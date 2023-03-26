class MicroArray:
    def __init__(self, data):
        self.data = data
        self.shape = (len(data), len(data[0]))

    def __getitem__(self, index):
        i, j = index
        return self.data[i][j]

    def __setitem__(self, index, value):
        i, j = index
        self.data[i][j] = value

    def __repr__(self):
        return str(self.data)

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape of two arrays are not the same")
        return MicroArray([[self[i, j] + other[i, j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape of two arrays are not the same")
        return MicroArray([[self[i, j] - other[i, j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __mul__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape of two arrays are not the same")
        return MicroArray([[self[i, j] * other[i, j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __truediv__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape of two arrays are not the same")
        return MicroArray([[self[i, j] / other[i, j] for j in range(self.shape[1])] for i in range(self.shape[0])])

    def __pow__(self, other):
        if isinstance(other, MicroArray):
            if self.shape != other.shape:
                raise ValueError("Shape of two arrays are not the same")
            return MicroArray([[self[i, j] ** other[i, j] for j in range(self.shape[1])] for i in range(self.shape[0])])
        elif isinstance(other, (int, float)):
            return MicroArray([[self[i, j] ** other for j in range(self.shape[1])] for i in range(self.shape[0])])
        else:
            raise TypeError("Unsupported operand type(s) for ** or pow()")

    def __eq__(self, other):
        if self.shape != other.shape:
            return False
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                if self[i, j] == other[i, j]:
                    continue
                else:
                    return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.shape[0])] for i in range(self.shape[1])]
        return MicroArray(transposed_data)

