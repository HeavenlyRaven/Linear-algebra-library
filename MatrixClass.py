from .VectorClass import Vector


class MatrixDimensionError(Exception):

    """ Error class for matrices """


class Matrix:

    """ Matrix class description """

    def __init__(self, data):

        if type(data) != list:
            raise TypeError("You can only pass a list to the Matrix constructor")

        for row in data:
            if type(row) != list:
                raise TypeError("You can only pass a list as a row")
            if any(not isinstance(x, (int, float)) for x in row):
                raise TypeError("Values of a matrix must be integers or floats")

        self.columns = 0
        self.rows = len(data)
        self.matrix_string = ""
        self.__data = []

        for row in data:
            self.__data.append(Vector(row))

        for row in data:
            self.columns = max(self.columns, len(row))

        for i in range(self.rows):
            if len(self.__data[i]) < self.columns:
                new_row_data = self.__data[i].data_copy()+([0]*(self.columns-len(self.__data[i])))
                self.__data[i] = Vector(new_row_data)

    def __str__(self):

        for row in self.__data:
            self.matrix_string += str(row)+"\n"

        return self.matrix_string

    def __eq__(self, other):

        if self.__data == other.__data:
            return True
        else:
            return False

    def __add__(self, other):

        if (self.rows != other.rows) or (self.columns != other.columns):
            raise MatrixDimensionError("Can't add two matrices with different dimensions")

        new_data = []

        for i in range(self.rows):
            new_data.append([])
            for j in range(self.columns):
                new_data[i].append(self.__data[i][j] + other.__data[i][j])

        return Matrix(new_data)

    def __sub__(self, other):

        if (self.rows != other.rows) or (self.columns != other.columns):
            raise MatrixDimensionError("Can't subtract one matrix from another: they must have the same dimension")

        new_data = []

        for i in range(self.rows):
            new_data.append([])
            for j in range(self.columns):
                new_data[i].append(self.__data[i][j] - other.__data[i][j])

        return Matrix(new_data)

    def __mul__(self, other):

        if type(other) == int or type(other) == float:

            new_data = []

            for i in range(self.rows):
                new_data.append([])
                for j in range(self.columns):
                    new_data[i].append(self.__data[i][j] * other)

            return Matrix(new_data)

        elif isinstance(other, Matrix):

            if self.columns != other.rows:
                raise MatrixDimensionError("Can't multiply two matrices:\
                 number of columns in the first matrix\
                  must equal the number of rows in the second matrix")

            new_data = []

            for i in range(self.rows):
                new_data.append([])
                for j in range(other.columns):
                    new_data[i].append(0)
                    for k in range(self.columns):
                        new_data[i][j] += self.__data[i][k] * other.__data[k][j]

            return Matrix(new_data)
        else:
            raise TypeError("Can only multiply two matrices or a matrix and a number")

    def __rmul__(self, other):

        if type(other) == int or type(other) == float:
            return self.__mul__(other)
        else:
            raise TypeError("Can only multiply two matrices or a matrix and a number")

    def __pow__(self, power):

        if power % 1 == 0 and power > 0:
            if self.rows == self.columns:
                new_matrix = self
                for i in range(power-1):
                    new_matrix *= self
                return new_matrix
            else:
                raise MatrixDimensionError("Only square matrices can be raised to a power")
        else:
            raise TypeError("Power must be positive integer")

    def __getitem__(self, item):

        return self.__data[item]

    def __setitem__(self, key, value):

        if isinstance(value, list):
            if len(self.__data[key]) == len(value):
                if all(isinstance(x, (int, float)) for x in value):
                    self.__data[key] = value
                else:
                    raise TypeError("Values of a row must be integers or floats")
            else:
                raise MatrixDimensionError("Can't assign a new row: the number of elements is not the same")
        else:
            raise TypeError("You can only pass a list as a new row")

    @property
    def transposed(self):

        new_data = []
        for j in range(self.columns):
            new_data.append([])
            for i in range(self.rows):
                new_data[j].append(self.__data[i][j])

        return Matrix(new_data)


class IdentityMatrix(Matrix):

    def __init__(self, n):

        if type(n) != int or n <= 0:
            raise TypeError("IdentityMatrix takes one positive integer as its dimension")

        identity_data = []

        for i in range(n):
            identity_data.append([])
            for j in range(n):
                identity_data[i].append(1 if i == j else 0)

        Matrix.__init__(self, identity_data)


class ZeroMatrix(Matrix):

    def __init__(self, n, m):

        if type(n) != int or type(m) != int or n <= 0 or m <= 0:
            raise TypeError("ZeroMatrix takes two positive integers as its dimensions")

        Matrix.__init__(self, [[0 for j in range(m)] for i in range(n)])

