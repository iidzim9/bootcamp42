class Matrix:
    def __init__(self, arg):
        if isinstance(arg, tuple):
            self.data=[]
            for i in range(0,arg[0]):
                for j in range(0,arg[1]):
                    self.data[i][j].append(i)
            # self.arg = [float(i,j) for i, j in zip(arg[0], arg[1])]
        else:
            self.arg = arg
        self.shape = (len(self.arg), len(self.arg[0]))

    def __add__(self, vect):
        pass

    def __radd__(self, vect):
        return self.__add__(vect)


    def __sub__(self, vect):
        pass

    def __rsub__(self, vect):
        return self.__sub__(vect) * (-1)

    def __truediv__(self, vect):
        pass

    def __rtruediv__(self, vect):
        pass

    def __mul__(self, vect):
        pass

    def __rmul__(self, vect):
        return self.__mul__(vect)

    def __str__(self):
        return 'Matrix: {self.data}\nShape: {self.shape}\n'.format(self=self)

    def __repr__(self):
        return '{self.data} {self.shape}'.format(self=self)
