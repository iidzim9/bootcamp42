class Matrix:
	def __init__(self, data):
		if isinstance(data, tuple):
			self.data = [list(range(data[1] * i, data[1] * (i + 1)))
            	for i in range(data[0])]
		else:
			self.data = data
		self.shape = (len(self.data), len(self.data[0]))


m2 = Matrix((3,12))

m1 = Matrix([[0.0, 1.0, 2.0, 3.0], 
                [0.0, 2.0, 4.0, 6.0]])
print(m2.data)
#			for i in range(0, data[0] * data[1]):
#				for j in range(0 , data[1]):
#					for z in range (0, data[0]):
#						self.data[j][z] = i
#						i += 1