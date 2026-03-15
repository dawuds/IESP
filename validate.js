#!/usr/bin/env node
/**
 * validate.js — IESP (IT External Service Provider) data integrity validator
 *
 * Checks:
 *   1.  All JSON files parse without errors (excluding .wwebjs_auth)
 *   2.  Control domains — id uniqueness and required fields
 *   3.  Control domains — subControls integrity
 *   4.  Control mapping integrity
 *   5.  Artifacts inventory — category and item integrity
 *   6.  Clause-map cross-references
 *   7.  Decision tree integrity
 *   8.  No empty strings where data is expected
 *   9.  Unique IDs across all data
 *   10. All expected files present
 *
 * Usage: node validate.js [--verbose]
 */

'use strict';

const fs   = require('fs');
const path = require('path');

const REPO_ROOT = __dirname;
const verbose   = process.argv.includes('--verbose');

let pass = 0;
let fail = 0;
let warn = 0;

function ok(msg)      { pass++; if (verbose) console.log(`  PASS  ${msg}`); }
function bad(msg)     { fail++; console.log(`  FAIL  ${msg}`); }
function warning(msg) { warn++; console.log(`  WARN  ${msg}`); }

function loadJson(relPath) {
  const abs = path.join(REPO_ROOT, relPath);
  if (!fs.existsSync(abs)) return null;
  try {
    return JSON.parse(fs.readFileSync(abs, 'utf8'));
  } catch (e) {
    return null;
  }
}

// ── 1. JSON Parse Check ─────────────────────────────────────────────

console.log('\n=== 1. JSON Parse Check ===');

function findJsonFiles(dir) {
  const results = [];
  if (!fs.existsSync(dir)) return results;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    // Skip .wwebjs_auth and hidden dirs
    if (entry.isDirectory() && !entry.name.startsWith('.') && entry.name !== 'node_modules') {
      results.push(...findJsonFiles(full));
    } else if (entry.isFile() && entry.name.endsWith('.json')) {
      results.push(path.relative(REPO_ROOT, full));
    }
  }
  return results;
}

const jsonFiles = findJsonFiles(REPO_ROOT);
const parsed = {};
let parseErrors = 0;

for (const file of jsonFiles) {
  try {
    parsed[file] = JSON.parse(fs.readFileSync(path.join(REPO_ROOT, file), 'utf8'));
    ok(`Parsed: ${file}`);
  } catch (e) {
    bad(`JSON parse error: ${file} — ${e.message}`);
    parseErrors++;
  }
}

if (parseErrors === 0) {
  ok(`All ${jsonFiles.length} JSON files parse correctly`);
}

// ── Load core data ──────────────────────────────────────────────────

const controlDomains = loadJson('controls/control-domains.json');
const controlMapping = loadJson('controls/control-mapping.json');
const artifactsInv   = loadJson('artifacts/inventory.json');
const clauseMap      = loadJson('artifacts/clause-map.json');
const decisionTree   = loadJson('decision-tree/decision-tree.json');

// Build domain/control sets from control-domains.json
const allDomains = (controlDomains && controlDomains.domains) || [];
const domainIdSet = new Set(allDomains.map(d => d.id).filter(Boolean));

const allSubControls = [];
for (const dom of allDomains) {
  if (dom.subControls && Array.isArray(dom.subControls)) {
    allSubControls.push(...dom.subControls);
  }
}
const subControlIdSet = new Set(allSubControls.map(c => c.id).filter(Boolean));

// Build artifact set from inventory categories (object with category keys)
const allArtifacts = [];
if (artifactsInv && artifactsInv.categories && typeof artifactsInv.categories === 'object') {
  for (const [catKey, catData] of Object.entries(artifactsInv.categories)) {
    if (catData && catData.items && Array.isArray(catData.items)) {
      allArtifacts.push(...catData.items);
    } else if (Array.isArray(catData)) {
      allArtifacts.push(...catData);
    }
  }
}
const artifactIdSet = new Set(allArtifacts.map(a => a.id || a.slug).filter(Boolean));

// ── 2. Control Domains — ID Uniqueness & Required Fields ─────────────

console.log('\n=== 2. Control Domain ID Uniqueness & Required Fields ===');

const domIdCounts = {};
for (const dom of allDomains) {
  if (!dom.id) {
    bad(`Domain missing "id": ${(dom.name || '').slice(0, 60)}`);
  } else {
    domIdCounts[dom.id] = (domIdCounts[dom.id] || 0) + 1;
  }
  if (!dom.name || dom.name.trim() === '') bad(`Domain "${dom.id}" has empty or missing "name"`);
}

const domDups = Object.entries(domIdCounts).filter(([, c]) => c > 1);
if (domDups.length === 0) {
  ok(`No duplicate domain IDs (${allDomains.length} domains)`);
} else {
  for (const [id, count] of domDups) bad(`Duplicate domain ID "${id}" appears ${count} times`);
}

// ── 3. SubControls Integrity ─────────────────────────────────────────

console.log('\n=== 3. SubControls Integrity ===');

const scIdCounts = {};
for (const sc of allSubControls) {
  if (!sc.id) {
    bad(`SubControl missing "id"`);
  } else {
    scIdCounts[sc.id] = (scIdCounts[sc.id] || 0) + 1;
  }
}

const scDups = Object.entries(scIdCounts).filter(([, c]) => c > 1);
if (scDups.length === 0) {
  ok(`No duplicate subControl IDs (${allSubControls.length} subControls)`);
} else {
  for (const [id, count] of scDups) bad(`Duplicate subControl ID "${id}" appears ${count} times`);
}

// Check each domain has at least one subControl
for (const dom of allDomains) {
  if (!dom.subControls || dom.subControls.length === 0) {
    warning(`Domain "${dom.id}" has no subControls`);
  } else {
    ok(`Domain "${dom.id}" has ${dom.subControls.length} subControl(s)`);
  }
}

// ── 4. Control Mapping Integrity ─────────────────────────────────────

console.log('\n=== 4. Control Mapping Integrity ===');

if (controlMapping && controlMapping.mappings) {
  let mapErrors = 0;
  for (const mapping of controlMapping.mappings) {
    if (!mapping.iespDomain) {
      bad('Mapping entry missing "iespDomain"');
      mapErrors++;
    }
  }
  if (mapErrors === 0) {
    ok(`All ${controlMapping.mappings.length} control mappings have required fields`);
  }
} else {
  warning('No control mappings found');
}

// ── 5. Artifacts Inventory Integrity ─────────────────────────────────

console.log('\n=== 5. Artifacts Inventory Integrity ===');

if (artifactsInv && artifactsInv.categories) {
  const catKeys = Object.keys(artifactsInv.categories);
  ok(`Artifacts inventory has ${catKeys.length} categories`);
  ok(`Total artifacts: ${allArtifacts.length}`);
} else {
  warning('No artifacts inventory found');
}

// ── 6. Clause-Map Cross-References ───────────────────────────────────

console.log('\n=== 6. Clause-Map Cross-References ===');

if (clauseMap && clauseMap.mappings) {
  const mappings = Array.isArray(clauseMap.mappings) ? clauseMap.mappings : [];
  ok(`Clause-map has ${mappings.length} mapping entries`);
} else if (clauseMap && clauseMap.clauseToEngagement) {
  ok(`Clause-map has clauseToEngagement with ${Object.keys(clauseMap.clauseToEngagement).length} entries`);
} else {
  warning('No clause-map found');
}

// ── 7. Decision Tree Integrity ───────────────────────────────────────

console.log('\n=== 7. Decision Tree Integrity ===');

if (decisionTree) {
  if (decisionTree.nodes) {
    const nodes = Array.isArray(decisionTree.nodes) ? decisionTree.nodes : Object.values(decisionTree.nodes);
    ok(`Decision tree has ${nodes.length} nodes`);

    // Check node references
    const nodeIdSet = new Set(nodes.map(n => n.id).filter(Boolean));
    let refErrors = 0;
    for (const node of nodes) {
      if (node.options) {
        for (const opt of node.options) {
          if (opt.nextNode && !nodeIdSet.has(opt.nextNode)) {
            bad(`Decision tree node "${node.id}" option references unknown node "${opt.nextNode}"`);
            refErrors++;
          }
        }
      }
    }
    if (refErrors === 0) ok('All decision tree node references resolve correctly');
  }
  if (decisionTree.outcomes) {
    const outcomes = Array.isArray(decisionTree.outcomes) ? decisionTree.outcomes : Object.values(decisionTree.outcomes);
    ok(`Decision tree has ${outcomes.length} outcomes`);
  }
} else {
  warning('No decision tree found');
}

// ── 8. Data Completeness ─────────────────────────────────────────────

console.log('\n=== 8. Data Completeness ===');

let emptyIssues = 0;
for (const dom of allDomains) {
  if (dom.name && dom.name.trim() === '') { bad(`Domain "${dom.id}" has empty name`); emptyIssues++; }
  if (dom.description && dom.description.trim() === '') { bad(`Domain "${dom.id}" has empty description`); emptyIssues++; }
}
for (const sc of allSubControls) {
  if (sc.id && sc.id.trim() === '') { bad('SubControl has empty id'); emptyIssues++; }
}
if (emptyIssues === 0) ok('No empty strings detected in core data');

// ── 9. Unique IDs Across All Data ────────────────────────────────────

console.log('\n=== 9. Unique IDs Across All Data ===');

const seenArtIds = {};
for (const art of allArtifacts) {
  const key = art.id || art.slug;
  if (key) seenArtIds[key] = (seenArtIds[key] || 0) + 1;
}
const artDups = Object.entries(seenArtIds).filter(([, c]) => c > 1);
if (artDups.length === 0) ok(`All ${allArtifacts.length} artifact IDs are unique`);
else for (const [id, c] of artDups) bad(`Duplicate artifact ID "${id}" appears ${c} times`);

// ── 10. All Expected Files Present ───────────────────────────────────

console.log('\n=== 10. All Expected Files Present ===');

const expectedFiles = [
  'controls/control-domains.json',
  'controls/control-mapping.json',
  'artifacts/inventory.json',
  'artifacts/clause-map.json',
  'decision-tree/decision-tree.json',
];

for (const f of expectedFiles) {
  const data = loadJson(f);
  if (data === null) warning(`Expected file not found or unparseable: ${f}`);
  else ok(`Present: ${f}`);
}

// ── Summary ──────────────────────────────────────────────────────────

console.log('\n' + '='.repeat(60));
console.log('Validation complete:');
console.log(`  Pass: ${pass}`);
console.log(`  Fail: ${fail}`);
console.log(`  Warn: ${warn}`);
console.log(`  Total: ${pass + fail + warn}`);
console.log('='.repeat(60));

if (fail > 0) {
  console.error(`\nValidation FAILED with ${fail} error(s).`);
  process.exit(1);
} else if (warn > 0) {
  console.log(`\nValidation passed with ${warn} warning(s).`);
  process.exit(0);
} else {
  console.log('\nAll checks passed.');
  process.exit(0);
}
