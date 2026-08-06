class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return self.__class__(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return self.__class__(x, y)

    def angle_between(self, other):
        import math
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        import math
        mul_vectors = self.__mul__(self.__class__(0, abs(self.y)))
        mul_length = self.get_length() * (
            self.__class__(0, abs(self.y)).get_length())
        cos_a = mul_vectors / mul_length
        return round(math.degrees(math.acos(cos_a)))

    def get_angle_x(self):
        import math
        mul_vectors = self.__mul__(self.__class__(abs(self.x), 0))
        mul_length = self.get_length() * (
            self.__class__(abs(self.x), 0).get_length())
        cos_a = mul_vectors / mul_length

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        import math
        x = (self.x * math.cos(math.radians(degrees)) - (
             self.y * math.sin(math.radians(degrees))))
        y = (self.x * math.sin(math.radians(degrees)) + (
             self.y * math.cos(math.radians(degrees))))
        return self.__class__(x, y)
