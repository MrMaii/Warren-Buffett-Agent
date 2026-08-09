import assert from 'node:assert/strict';
import test from 'node:test';

import {
  buildBehaviorRevisionPrompt,
  evaluateBehavior,
  getQualifiedFallback,
  sanitizeResponse,
} from '../runtime/qualityGate.js';

test('exports the persona-neutral quality-gate interface', () => {
  assert.equal(typeof evaluateBehavior, 'function');
  assert.equal(typeof buildBehaviorRevisionPrompt, 'function');
  assert.equal(typeof sanitizeResponse, 'function');
  assert.equal(typeof getQualifiedFallback, 'function');
});

test('allows calm ordinary conversation without forcing an investing framework', () => {
  const violations = evaluateBehavior(
    'Hello. I just want to talk for a minute.',
    'Of course. What has been taking up most of your attention today?',
    '',
  );
  assert.deepEqual(violations, []);
});

test('blocks guaranteed-profit concentration advice', () => {
  const user = 'Should I go all-in on this popular stock?';
  const draft = 'Yes. Put it all in; popularity guarantees the price will keep rising.';
  const violations = evaluateBehavior(user, draft, user);
  assert.ok(violations.length > 0);
  assert.match(violations.join('\n'), /market-timing|permanent capital loss|all-in|guarantee/i);
});

test('returns a bounded fallback for an all-in request', () => {
  const fallback = getQualifiedFallback(
    'Should I go all-in on this popular stock?',
    '',
  );
  assert.match(fallback, /Do not put all of your capital into it/i);
  assert.match(fallback, /reversible next step/i);
});

test('builds a revision prompt from observed violations', () => {
  const prompt = buildBehaviorRevisionPrompt(
    { interactionMode: 'high-stakes' },
    ['Invented a market-timing probability without current evidence.'],
    'Should I buy now?',
  );
  assert.match(prompt, /market-timing probability/i);
  assert.match(prompt, /current primary data/i);
});

test('sanitizer preserves bounded normal content', () => {
  const content = 'Protect obligations first, then compare this decision with the next-best use of the money.';
  assert.equal(sanitizeResponse('Help me compare two options.', content), content);
});
