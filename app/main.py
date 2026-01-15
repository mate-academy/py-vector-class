import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start, end):
        point_x = end[0] - start[0]
        point_y = end[1] - start[1]
        return cls(point_x, point_y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other):
        res = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(res)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle):
        converted = math.radians(angle)
        new_x = math.cos(converted) * self.x - math.sin(converted) * self.y
        new_y = math.sin(converted) * self.x + math.cos(converted) * self.y
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)
        return self
