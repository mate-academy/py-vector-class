import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return cls(cls.x, cls.y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        lengthsv = self.get_length()
        return Vector(
            x=self.x / lengthsv,
            y=self.y / lengthsv
        )

    def angle_between(self, other):
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        yaxis = self.y - self.x
        cos_a = (self.y * yaxis) / (self.get_length() * yaxis)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        return Vector(
            x=(math.cos(radians) * self.x) - (math.sin(radians) * self.y),
            y=(math.sin(radians) * self.x) + (math.cos(radians) * self.y)
        )
