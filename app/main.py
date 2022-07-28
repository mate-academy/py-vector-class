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
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(*end_point) - Vector(*start_point)

    def get_length(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x * (1 / length), self.y * (1 / length))

    def angle_between(self, other):
        ab_mul = self * other
        a_len = self.get_length()
        b_len = other.get_length()
        return round(math.degrees(math.acos(ab_mul / (a_len * b_len))))

    def get_angle(self):
        axis_y = Vector(0, 1)
        return self.angle_between(axis_y)

    def rotate(self, degrees):
        cs = math.cos(math.radians(degrees))
        sn = math.sin(math.radians(degrees))
        x = self.x * cs - self.y * sn
        y = self.x * sn + self.y * cs
        return Vector(x, y)
