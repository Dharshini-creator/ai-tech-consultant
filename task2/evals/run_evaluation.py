import json
import sys
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TASK_DIR))

from src.inbox_agent import analyze_email

cases_file = Path(__file__).with_name("inbox_cases.json")
cases = json.loads(cases_file.read_text(encoding="utf-8-sig"))

passed = 0
results = []

for case in cases:
    actual = analyze_email(case["email"])

    priority_ok = actual["priority"] == case["expected_priority"]
    category_ok = actual["category"] == case["expected_category"]
    review_ok = (
        actual["review_status"] == "pending"
        and actual["approved"] is False
    )

    case_passed = priority_ok and category_ok and review_ok
    passed += int(case_passed)

    results.append({
        "id": case["id"],
        "expected_priority": case["expected_priority"],
        "actual_priority": actual["priority"],
        "priority_pass": priority_ok,
        "expected_category": case["expected_category"],
        "actual_category": actual["category"],
        "category_pass": category_ok,
        "review_pass": review_ok,
        "passed": case_passed
    })

output_file = Path(__file__).with_name("inbox_results.json")
output_file.write_text(json.dumps(results, indent=2), encoding="utf-8")

print(f"Total cases: {len(cases)}")
print(f"Passed: {passed}")
print(f"Failed: {len(cases) - passed}")
print(f"Pass rate: {passed / len(cases) * 100:.1f}%")
print("\nCase results:")

for result in results:
    status = "PASS" if result["passed"] else "FAIL"
    print(
        f'{result["id"]}: {status} | '
        f'priority={result["actual_priority"]} | '
        f'category={result["actual_category"]}'
    )

print(f"\nDetailed results saved to: {output_file}")
