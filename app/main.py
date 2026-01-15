import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(x=self.x * other, y=self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length())

    def angle_between(self, other):
        return round(math.degrees(
            math.acos(
                (self * other) / (self.get_length() * other.get_length()))))

    def get_angle(self):
        other = Vector(0, 1)
        return round(math.degrees(
            math.acos(
                (self * other) / (self.get_length() * other.get_length()))))

    def rotate(self, angle):
        cs = math.cos(math.radians(angle))
        sn = math.sin(math.radians(angle))
        return Vector(x=self.x * cs - self.y * sn, y=self.x * sn + self.y * cs)
