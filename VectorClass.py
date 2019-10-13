class Vector:

    """ Vector class description """

    def __init__(self, data):

        if type(data) != list:
            raise TypeError("You can only pass a list to the Vector constructor")

        for element in data:
            if not isinstance(element, (int, float)):
                raise TypeError("Values of a vector must be integers or floats")

        self.__data = data

    def __str__(self):

        return "\t".join(list(map(str, self.__data)))

    def __repr__(self):

        return repr(self.__data)

    def __abs__(self):

        length_squared = 0
        for element in self.__data:
            length_squared += element*element

        return length_squared**0.5

    def __len__(self):

        return len(self.__data)

    def __getitem__(self, item):

        return self.__data[item]

    def __setitem__(self, key, value):

        if not isinstance(value, (int, float)):
            raise TypeError("Values of a vector must be integers or floats")

        self.__data[key] = value

    def __copy__(self):

        return Vector(self.__data.copy())

    def data_copy(self):

        return self.__data.copy()
