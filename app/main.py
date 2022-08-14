from math import acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        x = round(self.x + other.x, 2)
        y = round(self.y + other.y, 2)
        return Vector(x, y)

    def __sub__(self, other):
        x = round(self.x - other.x, 2)
        y = round(self.y - other.y, 2)
        return Vector(x, y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return Vector(x, y)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_points: tuple,
                                    end_points: tuple):
        x = round(end_points[0] - start_points[0], 2)
        y = round(end_points[1] - start_points[1], 2)
        return cls(x, y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        x = round(self.x / self.get_length(), 2)
        y = round(self.y / self.get_length(), 2)
        return Vector(x, y)

    def angle_between(self, other):
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle):
        x = cos(radians(angle)) * self.x - sin(radians(angle)) * self.y
        y = cos(radians(angle)) * self.y + sin(radians(angle)) * self.x
        return Vector(x, y)
