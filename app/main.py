import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other_vector):
        return Vector(
            self.x + other_vector.x,
            self.y + other_vector.y
        )

    def __sub__(self, other_vector):
        return Vector(
            self.x - other_vector.x,
            self.y - other_vector.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        if self.get_length() != 0:
            return self * (1.0 / self.get_length())
        return Vector(0, 0)

    def angle_between(self, other):
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        x = self.x * math.cos(math.radians(degrees)) - \
            self.y * math.sin(math.radians(degrees))
        y = self.x * math.sin(math.radians(degrees)) + \
            self.y * math.cos(math.radians(degrees))
        return Vector(x, y)
