# Demo Steps

1. Create a new GitHub repository (e.g. `bug-prediction-ci`).
2. Upload or push all project files, keeping the `.github/workflows/` folder structure.
3. Open the **Actions** tab. The "Bug Prediction CI" workflow starts automatically.
4. Open the finished run. The **Summary** page shows the bug report (risk: LOW).
5. Download the `bug-report` artifact to show the saved report.
6. **Show a failure:** edit `app.py` and change `return a + b` to `return a - b`. Commit and push.
7. The pytest step fails and the predictor reports MEDIUM risk.
8. **Show HIGH risk:** also add a badly formatted line to `app.py` (e.g. `x=1;y=2`) so flake8 fails too.
9. Revert the changes to return to LOW risk.

Note: the pytest and flake8 steps fail the job on their own; the predictor step still runs
(`if: always()`) so the report is produced either way.
