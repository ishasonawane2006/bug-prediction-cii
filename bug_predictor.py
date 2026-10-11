"""Rule-based bug risk predictor for CI.

Runs three checks and counts how many fail:
  1. Syntax check  (python -m compileall)
  2. Unit tests    (pytest)
  3. Lint          (flake8)

Failed checks -> Bug risk:  0 = LOW, 1 = MEDIUM, 2+ = HIGH

This is an educational rule-based model, not machine learning.
Usage: python bug_predictor.py [--fail-on-high]
"""
import subprocess
import sys
from datetime import datetime, timezone

CHECKS = [
    ("Syntax check", [sys.executable, "-m", "compileall", "-q", "."]),
    ("Unit tests (pytest)", [sys.executable, "-m", "pytest", "-q"]),
    ("Lint (flake8)", [sys.executable, "-m", "flake8", ".", "--max-line-length=100",
                       "--exclude=.git,__pycache__,.venv"]),
]


def run_check(name, command):
    result = subprocess.run(command, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    return {"name": name, "passed": result.returncode == 0, "output": output}


def predict_risk(failed_count):
    if failed_count == 0:
        return "LOW", "🟢"
    if failed_count == 1:
        return "MEDIUM", "🟡"
    return "HIGH", "🔴"


def build_report(results):
    failed = sum(1 for r in results if not r["passed"])
    risk, icon = predict_risk(failed)
    lines = [
        "# Bug Prediction Report",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        f"**Failed checks:** {failed} / {len(results)}",
        f"**Predicted bug risk:** {icon} {risk}",
        "",
        "| Check | Status |",
        "|---|---|",
    ]
    for r in results:
        lines.append(f"| {r['name']} | {'✅ Passed' if r['passed'] else '❌ Failed'} |")
    for r in results:
        if not r["passed"]:
            lines += ["", f"## Details: {r['name']}", "```", r["output"][-2000:], "```"]
    return "\n".join(lines) + "\n", risk


def main():
    results = [run_check(name, cmd) for name, cmd in CHECKS]
    report, risk = build_report(results)
    with open("bug_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    if "--fail-on-high" in sys.argv and risk == "HIGH":
        sys.exit(1)


if __name__ == "__main__":
    main()
