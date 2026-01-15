import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self):
        return Vector(
            self.x / ((self.x ** 2 + self.y ** 2) ** (1 / 2)),
            self.y / ((self.x ** 2 + self.y ** 2) ** (1 / 2))
        )

    def angle_between(self, other):
        cos_angle = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self):
        product = self.y * self.y
        cos_angle = product / ((self.x ** 2 + self.y ** 2) ** 0.5 * self.y)
        return int(math.degrees(math.acos(cos_angle)))

    def rotate(self, degree):
        cos_angle = math.cos(math.radians(degree))
        sin_angle = math.sin(math.radians(degree))
        return Vector(
            cos_angle * self.x - sin_angle * self.y,
            sin_angle * self.x + cos_angle * self.y,
        )
