# Report Content: Bug Prediction using GitHub Actions

## 1. Title
Automated Bug Risk Prediction using GitHub Actions CI

## 2. Aim
To implement a mini project using a DevOps tool (GitHub Actions) that automatically checks code
quality on every commit and predicts the bug risk of the code.

## 3. Objectives
- Automate testing and linting on every push and pull request.
- Predict bug risk from check results.
- Produce a downloadable bug report for each build.

## 4. Tools and Technologies
Python 3.11, PyTest, Flake8, Git, GitHub, GitHub Actions.

## 5. Theory
- **CI/CD:** Continuous Integration builds and tests code automatically on each change.
- **GitHub Actions:** GitHub's workflow automation, defined in YAML under `.github/workflows/`.
- **Unit testing (PyTest):** verifies that functions behave as expected.
- **Static analysis (Flake8):** detects style and simple code errors without running code.
- **Defect prediction:** estimating the likelihood of bugs from measurable indicators.

## 6. System Design
Code Push -> GitHub -> GitHub Actions -> Tests -> Flake8 -> Bug Predictor -> Bug Report

## 7. Implementation
- `app.py`: sample functions (add, subtract, multiply, divide, is_palindrome).
- `test_app.py`: 7 PyTest unit tests.
- `bug_predictor.py`: runs syntax check, pytest and flake8, counts failures, assigns risk.
- `bug-prediction.yml`: workflow that installs dependencies, runs all checks, publishes the
  report to the job summary and uploads it as an artifact.

## 8. Risk Model
0 failed checks = LOW, 1 = MEDIUM, 2 or more = HIGH. Rule-based, not machine learning.

## 9. Results
Include screenshots of: (a) green workflow run with LOW risk, (b) failing run with MEDIUM/HIGH
risk, (c) the bug report summary.

## 10. Advantages
Early bug detection, no manual testing effort, consistent quality gate, free for public repos.

## 11. Limitations and Future Scope
Risk depends only on pass/fail counts. Future work: add code complexity (radon), code churn,
test coverage, and train an ML model on historical commit data.

## 12. Conclusion
GitHub Actions can automate quality checks and give a simple, clear bug risk prediction on every
commit, demonstrating core DevOps CI practice.
