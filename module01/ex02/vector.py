class Vector:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.values = [float(i) for i in range(0, arg)]
        elif isinstance(arg, list):
            self.values = [float(i)  for i in arg]
        elif isinstance(arg, tuple):
            self.values = [float(i) for i in range(arg[0], arg[1])]
        self.size = len(self.values)

    def print_vect(self):
        print(self.values)

    def __add__(self, Scalar):
        new_vect=[]
        for v in self.values:
            new_vect.append(v + Scalar)
        return new_vect

    def __radd__(self, Scalar):
        return self.__add__(Scalar)

    def __sub__(self, Scalar):
        new_vect=[]
        for v in self.values:
            new_vect.append(v - Scalar)
        return new_vect

    def __rsub__(self, Scalar):
        new_vect=[]
        for v in self.values:
            new_vect.append(Scalar - v)
        return new_vect

    def __mul__(self, Scalar):
        new_vect=[]
        for v in self.values:
            new_vect.append(Scalar * v)
        return new_vect

    def __rmul__(self, Scalar):
        return self.__mul__(Scalar)

    def __truediv__(self, Scalar):
        new_vect=[]
        for v in self.values:
            new_vect.append(v / Scalar)
        return new_vect

    def __rtruediv__(self, Scalar):
        new_vect=[]
        for v in self.values:
            new_vect.append(Scalar / v)
        return new_vect

    def __str__(self):
        return 'vector: {self.values}\nsize: {self.size}\n'.format(self=self)
    
    def __repr__(self):
        return '{self.values} {self.size}'.format(self=self)
