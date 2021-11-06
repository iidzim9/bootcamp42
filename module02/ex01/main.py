def what_are_the_vars(*args, **keywargs):
	o = ObjectC()
	if args:
		for i, val in zip(range(len(args)), args):
			setattr(o, f"var_{i}", val)
	if keywargs:
		for key in keywargs.keys():
			if "var_" in key:
				return None
			else:
				setattr(o, key, keywargs.get(key))
	return o

class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":

	# test1 = dict()
	# test = {"key" : "value", "a" : "b"}
	# print(test.get("keysdfs", 10))

	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
