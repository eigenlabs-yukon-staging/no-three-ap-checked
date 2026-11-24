import json
import sys

numbers = json.load(sys.stdin)["set"]
values = set(numbers)
in_range = all(1 <= n <= 50 for n in numbers) and len(values) == len(numbers)
progression = any(2 * b - a in values for a in values for b in values if a < b)
print(json.dumps({"passed": in_range and not progression, "size": len(numbers)}))
