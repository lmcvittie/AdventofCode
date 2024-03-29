from typing import Dict, List

def ssort(unsorted: str) -> str:
	return str.join("", sorted(list(unsorted)))

def decode(inputs: List[str]) -> Dict[str, int]:
	inputs.sort(key=lambda x: len(x))
	one = inputs[0]
	seven = inputs[1]
	four = inputs[2]
	eight = inputs[9]
	
	length_six = inputs[6:-1]
	for elem in length_six:
		if not one[0] in elem:
			six = elem
			length_six.remove(elem)
			seg_c = one[0]
			seg_f = one[1]
			break
		if not one[1] in elem:
			six = elem
			length_six.remove(elem)
			seg_c = one[1]
			seg_f = one[0]
			break
	else:
		raise Exception("6 not found")

	for elem in length_six:
		options = [c for c in list(four) if c not in one]
		if not options[0] in elem or not options[1] in elem:
			zero = elem
			length_six.remove(elem)
			break
	else:
		raise Exception("0 not found")

	nine = length_six[0]

	for elem in inputs[3:-4]:
		if seg_c not in elem:
			five = elem
		elif seg_f not in elem:
			two = elem
		else:
			three = elem
	assert five
	assert two
	assert three

	return {
		one: 1,
		two: 2,
		three: 3,
		four: 4,
		five: 5,
		six: 6,
		seven: 7,
		eight: 8,
		nine: 9,
		zero: 0,
	}


def run(input_data: List[str], **kwargs) -> int:
	total = 0
	for datum in input_data:
		inputs, outputs = datum.split(" | ")
		inputs = [ssort(e) for e in inputs.split(" ")]
		decoded = decode(inputs)
		outputs = [ssort(e) for e in outputs.split(" ")]
		total += decoded[outputs[0]] * 1000
		total += decoded[outputs[1]] * 100
		total += decoded[outputs[2]] * 10
		total += decoded[outputs[3]] * 1
	return total
