import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"{other} is not {type(Vector)}")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"{other} is not {type(Vector)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"{other} is not {type(Vector)} or {(int, float)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        vector_len = self.get_length()
        return Vector(self.x / vector_len, self.y / vector_len)

    def angle_between(self, other):
        a_cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(a_cos)))

    def get_angle(self):
        a_cos = self.y / self.get_length()
        return round(math.degrees(math.acos(a_cos)))

    def rotate(self, degrees):
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        x = self.x * cos - self.y * sin
        y = self.x * sin + self.y * cos
        return Vector(x, y)
