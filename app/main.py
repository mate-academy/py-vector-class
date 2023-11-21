import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        # a = 1 / self.get_length()
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, other):
        return round(math.degrees(math.acos((self * other) / (self.get_length() * other.get_length()))), 0)

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: float):
        return Vector(
            x=math.cos(math.radians(angle)) * self.x - math.sin(math.radians(angle)) * self.y,
            y=math.sin(math.radians(angle)) * self.x + math.cos(math.radians(angle)) * self.y,
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(list(end_point)[0] - list(start_point)[0], list(end_point)[1] - list(start_point)[1])























