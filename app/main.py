import math as mt


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return mt.sqrt(self.x**2 + self.y ** 2)

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        len2 = mt.sqrt(other.x ** 2 + other.y ** 2)
        x = self.get_length()
        return round(mt.degrees(mt.acos(self.__mul__(other) / (x * len2))))

    def get_angle(self):
        return round(mt.degrees(mt.acos(self.y / self.get_length())))

    def rotate(self, degree):
        rad = mt.radians(degree)
        return Vector(
            x=mt.cos(rad) * self.x - mt.sin(rad) * self.y,
            y=mt.sin(rad) * self.x + mt.cos(rad) * self.y,
        )
