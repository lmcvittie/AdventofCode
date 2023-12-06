from typing import List


def get_distance(time: int, time_held: int) -> int:
	return (time - time_held) * time_held


def lower_search(time: int, dist: int) -> int:
	lower_bound = 0
	upper_bound = time
	while True:
		time_held_test = int((upper_bound-lower_bound)/2) + lower_bound
		test_dist = get_distance(time, time_held_test)
		one_lower = get_distance(time, time_held_test-1)
		if test_dist > dist and one_lower <= dist:
			return time_held_test
		assert upper_bound - lower_bound > 1
		if test_dist > dist:
			upper_bound = time_held_test 
		else:
			lower_bound = time_held_test

def upper_search(time: int, dist: int) -> int:
	lower_bound = 0
	upper_bound = time
	while True:
		time_held_test = int((upper_bound-lower_bound)/2) + lower_bound
		test_dist = get_distance(time, time_held_test)
		one_lower = get_distance(time, time_held_test-1)
		if test_dist <= dist and one_lower > dist:
			return time_held_test
		assert upper_bound - lower_bound > 1
		if test_dist > dist:
			lower_bound = time_held_test
		else:
			upper_bound = time_held_test


def run(input_data: List[str], **kwargs) -> int:
	time = int(input_data[0].split(":")[1].replace(" ", ""))
	distance = int(input_data[1].split(":")[1].replace(" ", ""))
	lower = lower_search(time, distance)
	upper = upper_search(time, distance)
	return upper - lower