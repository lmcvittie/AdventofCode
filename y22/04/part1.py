from typing import List

def run(input_data: List[str]) -> int:
	count = 0
	for d in input_data:
		r1, r2 = d.split(",")
		min1, max1 = [int(a) for a in r1.split("-")]
		min2, max2 = [int(a) for a in r2.split("-")]
		if (
			(min1 <= min2 and max1 >= max2) or
			(min2 <= min1 and max2 >= max1)
		):
			count += 1
	return count