class VectorDimensionError(Exception):

    """

    Error class for Vector.
    """


class Vector:

    """

    Vector class.

    If no argument is given, the constructor rises TypeError.
    The argument must be a list.
    """

    def __init__(self, data):

        if type(data) != list:
            raise TypeError("You can only pass a list to the Vector constructor")

        for element in data:
            if not isinstance(element, (int, float)):
                raise TypeError("Values of a vector must be integers or floats")

        self.__data = data

    def __str__(self):

        """

        :return: String representation of a vector object.
        """

        return "\t".join(list(map(str, self.__data)))

    def __repr__(self):

        """

        :return: repr(self)
        """

        return repr(self.__data)

    def __abs__(self):

        """

        :return: Absolute of self.
        """

        length_squared = 0
        for element in self.__data:
            length_squared += element*element

        return length_squared**0.5

    def __len__(self):

        """

        :return: Number of elements in self.
        """

        return len(self.__data)

    def __eq__(self, other):

        """

        :param other: Vector object.
        :return: self==other.
        """

        return self.__data == other.__data

    def __add__(self, other):

        """

        :param other: Vector object.
        :return: self+other.
        """

        if isinstance(other, Vector):

            if len(self) == len(other):
                return Vector(self.__data[i] + other.__data[i] for i in range(len(self)))
            else:
                raise VectorDimensionError("For addition number of elements in vectors must be equal")

        else:
            raise TypeError("You can only add a vector to a vector")

    def __sub__(self, other):

        """

        :param other: Vector object.
        :return: self-other.
        """

        if isinstance(other, Vector):

            if len(self) == len(other):
                return Vector(self.__data[i] - other.__data[i] for i in range(len(self)))
            else:
                raise VectorDimensionError("For subtraction number of elements in vectors must be equal")

        else:
            raise TypeError("You can only subtract a vector from a vector")

    def __mul__(self, other):

        """

        :param other: Vector object.
        :return: Number equaled scalar multiplication of self and other (dot product).
        """

        if isinstance(other, (int, float)):

            return Vector([x*other for x in self.__data])

        elif isinstance(other, Vector):

            if len(self) == len(other):
                return sum(self.__data[i]*other.__data[i] for i in range(len(self)))
            else:
                raise VectorDimensionError("For scalar multiplication number of elements in vectors must be equal")
        else:
            raise TypeError("You can only multiply two vectors or a vector and a number")

    def __rmul__(self, other):

        """

        :param other: Vector object.
        :return: Number equaled scalar multiplication of other and self (dot product).
        """

        return self.__mul__(other)

    def __getitem__(self, item):

        """

        :param item: int
        :return: self element at {item} index.
        """

        return self.__data[item]

    def __setitem__(self, key, value):

        """

        :param key: int
        :param value: int OR float
        """

        if not isinstance(value, (int, float)):
            raise TypeError("Values of a vector must be integers or floats")

        self.__data[key] = value

    def list(self):

        """

        :return: Listed self.__data
        """

        return self.__data.copy()
    
    def v_mul_std(self, other):

        """

        :param other: Vector object.
        :return: Cross product (standard basis).
        """

        if not isinstance(other, Vector):
            raise TypeError("You can only multiply two vectors")
        if len(self) != len(other) != 3:
            return VectorDimensionError("For vector multiplication number of elements in vectors must equal 3")

        x = self[2]*other[3] - other[2]*self[3]
        y = self[3]*other[1] - other[3]*self[1]
        z = self[1]*other[2] - other[1]*self[2]

        return Vector([x, y, z])
