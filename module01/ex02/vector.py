class Vector:
    def __init__(self, arg):
        if isinstance(arg, int):
            self.values = [float(i) for i in range(0, arg)]
        elif isinstance(arg, list):
            self.values = [float(i)  for i in arg]
        elif isinstance(arg, tuple):
            self.values = [float(i) for i in range(arg[0], arg[1])]

    def print_vect(self):
        print(self.values, sep='->')

    def __add__(self, Scalar):
        pass

    def __radd__(self, Scalar):
        pass

    def __sub__(self, Scalar):
        pass

    def __rsub__(self, Scalar):
        pass

    def __truediv__(self, Scalar):
        pass

    def __rtruediv__(self, Scalar):
        pass