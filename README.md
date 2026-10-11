# Bug Prediction using GitHub Actions (ASDD Experiment 11 Mini Project)

A small CI/CD project that runs on every push or pull request and predicts bug risk
from the results of automated checks.

## Pipeline
Code Push -> GitHub -> GitHub Actions -> Tests -> Flake8 -> Bug Predictor -> Bug Report

## Files
| File | Purpose |
|---|---|
| app.py | Sample application (calculator + palindrome checker) |
| test_app.py | PyTest unit tests |
| bug_predictor.py | Rule-based bug risk predictor and report generator |
| requirements.txt | pytest, flake8 |
| .github/workflows/bug-prediction.yml | GitHub Actions workflow |

## Risk model
| Failed checks (syntax, tests, lint) | Bug risk |
|---|---|
| 0 | LOW |
| 1 | MEDIUM |
| 2+ | HIGH |

This is a rule-based educational model, not machine learning.

## Run locally
```
pip install -r requirements.txt
pytest
flake8 . --max-line-length=100
python bug_predictor.py
```
The report is written to `bug_report.md`.

## Run on GitHub
See DEMO_STEPS.md.
