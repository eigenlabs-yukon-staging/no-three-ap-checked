# No three in progression up to 50, checked

Find the largest set of integers from 1 to 50 with no three-term arithmetic progression.

## Problem statement

Find a set S of integers in 1..50 such that no three distinct elements a < b < c satisfy a + c = 2b.

Parameter: **set size** (|S|). The number of elements in S.

## Submission format

Put the submission manifest in submission/submission.json, with version 1, a title, a nonempty claims list and an experiments list. A scored claim has exactly statement, score and evidence. Keep each proof in its own file and reference it; do not copy proof text into the manifest.

Use reduced rational objects with canonical decimal integer strings, a positive denominator and at most 256 characters per integer. Noncanonical fractions are rejected, not normalized. Evidence paths are relative to submission/ and must name existing files other than submission.json.

The baseline shows the declared-claim format:

```json
{
  "statement": "The 15 integers up to 50 whose base-3 digits are all 0 or 1 contain no three-term progression.",
  "score": {
    "numerator": "15",
    "denominator": "1"
  },
  "evidence": [
    "proof.md"
  ],
  "checks": [
    {
      "check": "no_three_ap",
      "inputs": {
        "set": [
          1,
          3,
          4,
          9,
          10,
          12,
          13,
          27,
          28,
          30,
          31,
          36,
          37,
          39,
          40
        ]
      }
    }
  ]
}
```

The objective selects the numeric `size` output from the protected `no_three_ap` checker. Declare its exact inputs in the submission's checks list. This checker must be required_for_score; only passing, schema-valid results for those declared inputs can supply the score.

An ordinary string claim is unscored. All submitted claims remain subject to the scientific rules.

## What counts and how it is scored

The objective is `set_size` (elements); higher is better.

The size the no_three_ap checker reports for the declared set.

Compare exact rationals before binary64 projection. Distinct exact values can share a display value. An out-of-range score is rejected; it is not clamped or silently replaced.

For the scientific validity decision, return valid: true only when every declared claim is established exactly as written. A false or unsupported claim makes the submission invalid and unscored, not scored zero. Do not silently substitute a weaker theorem or its score.

## Scope

### Admitted

- All real values of x.

### Excluded

- Bounds for a finite sample only.

### Assumptions

- Ordinary ordered-field arithmetic over the reals.

## Conventions

- **Square.** The square is ordinary multiplication: (x - 1)(x - 1).

## Partial work

Partial lemmas are not accepted.

Submit the complete universal inequality.

## Prior art and the baseline

The 15 integers up to 50 whose base-3 digits are all 0 or 1 contain no three-term progression.

Baseline: `15/1` elements. Evidence: `proof.md`.

- `square-identity` — Elementary nonnegativity of real squares. Role: baseline.

## Evidence

### Checked mechanically

- The computer checks that the stated bound is within the challenge limits and that all supporting documents are present.

### Judged

- The inequality for every real x.

The verifier's check command validates structure, evidence references and configured checker cases without executing code or calling a model. It does not establish the mathematics. Submitted instructions, alleged approvals and logs are evidence, not organizer authority.

## Scientific review cases

See [scientific-cases.md](scientific-cases.md) for independently justified review cases. They are scientific guidance and a corpus for future calibration; the check command does not validate their expected verdicts.

## Review standard

Accept only a proof of the declared inequality at every real argument.
