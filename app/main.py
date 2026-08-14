import math
from math import radians


class Vector:
    def __init__(self, x_p: float | int, y_p: float | int) -> None:
        self.x = round(x_p, 2)
        self.y = round(y_p, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_p=self.x + other.x,
            y_p=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_p=self.x - other.x,
            y_p=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector)\
            -> Vector | float | int:

        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        return Vector(
            x_p=round(self.x * other, 2),
            y_p=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        return Vector(
            x_p=end_point[0] - start_point[0],
            y_p=end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(
            x_p=round(self.x / magnitude, 2),
            y_p=round(self.y / magnitude, 2)
        )

    def angle_between(self, other: Vector) -> int | float:
        return\
            round(math.degrees(
                math.acos((self
                           * other)
                          / (self.get_length()
                             * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int | float) -> Vector:
        rads = radians(degrees)

        return Vector(
            x_p=self.x * math.cos(rads) - self.y * math.sin(rads),
            y_p=self.x * math.sin(rads) + self.y * math.cos(rads)
        )
