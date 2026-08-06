import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(self.x * other,
                          self.y * other)
        return abs(self.x * other.x) - abs(self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self):
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other):
        cos_a = (self.x * other.x + self.y * other.y) / \
                (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_b = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_b)))

    def rotate(self, degrees):
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        return Vector(
            self.x * cos_a - self.y * sin_a,
            self.x * sin_a + self.y * cos_a
        )
