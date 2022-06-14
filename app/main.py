import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start_point, end_point):

        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1],
        )

    def get_length(self):
        return (self.x**2 + self.y**2) ** (1 / 2)

    def get_normalized(self):
        vector_length = self.get_length()

        return Vector(
            x=self.x / vector_length,
            y=self.y / vector_length,
        )

    def angle_between(self, other):
        prod = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        cos_a = prod / (abs(len_self) * abs(len_other))

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        rad = math.radians(degrees)
        cs = math.cos(rad)
        sn = math.sin(rad)
        x = self.x * cs - self.y * sn
        y = self.x * sn + self.y * cs

        return Vector(x, y)
