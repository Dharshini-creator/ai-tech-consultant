import json
import sys
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TASK_DIR))

from agents.scope_agent import create_scope

eval_dir = Path(__file__).resolve().parent
cases = json.loads(
    (eval_dir / "scope_cases.json").read_text(encoding="utf-8-sig")
)

results = []

for case in cases:
    actual = create_scope(case["meeting_notes"])

    expected = {
        "requirements": case["expected_requirements"],
        "deliverables": case["expected_deliverables"],
        "open_questions": case["expected_open_questions"],
    }

    actual_counts = {
        "requirements": len(actual["requirements"]),
        "deliverables": len(actual["deliverables"]),
        "open_questions": len(actual["open_questions"]),
    }

    passed = actual_counts == expected

    results.append({
        "id": case["id"],
        "expected": expected,
        "actual": actual_counts,
        "passed": passed,
    })

passed_count = sum(item["passed"] for item in results)
total = len(results)

(eval_dir / "scope_results.json").write_text(
    json.dumps(results, indent=2),
    encoding="utf-8",
)

print(f"Total cases: {total}")
print(f"Passed: {passed_count}")
print(f"Failed: {total - passed_count}")
print(f"Pass rate: {passed_count / total * 100:.1f}%" if total else "No cases found")

for item in results:
    print(f'{item["id"]}: {"PASS" if item["passed"] else "FAIL"}')

print(f"Results saved to: {eval_dir / 'scope_results.json'}")
