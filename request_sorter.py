import pprint
import operator

file_ = input('File to sort: ')

data = {}


def increment(a):
	"""
	Adds 1 to the global dictionary 'data' key a.
	"""
	global data
	try:
		data[a] += 1
	except KeyError:
		data.update({a: 1})


with open(file_, 'r') as f:
	for line in f:
		increment(line)

# pprint.pprint(data)

sorted_ = sorted(data.items(), key=operator.itemgetter(1))

pprint.pprint(sorted_)
