# Presentation Content (8 slides)

**Slide 1 – Title:** Bug Prediction using GitHub Actions | ASDD Experiment 11 | Name, Roll No.

**Slide 2 – Problem:** Bugs found late are costly. Manual checks are slow and inconsistent.

**Slide 3 – Solution:** Automate checks on every push with GitHub Actions and predict bug risk.

**Slide 4 – Architecture:** Code Push -> GitHub -> GitHub Actions -> Tests -> Flake8 -> Bug Predictor -> Bug Report

**Slide 5 – Tools:** Python, PyTest, Flake8, Git/GitHub, GitHub Actions (YAML workflow).

**Slide 6 – Risk Model:** 0 failed checks = LOW | 1 = MEDIUM | 2+ = HIGH (rule-based, not ML).

**Slide 7 – Demo:** Green run (LOW) -> break a test (MEDIUM) -> break lint too (HIGH). Show report artifact.

**Slide 8 – Conclusion and Future Scope:** Automated quality gate achieved. Next: complexity, churn,
coverage, ML-based prediction.
