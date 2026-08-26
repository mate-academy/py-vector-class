from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None: # noqa
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int | float:
        dot_prod = self * vector
        return round(math.degrees(math.acos(dot_prod
                                            / (self.get_length()
                                               * vector.get_length()))))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int | float) -> Vector:
        math_radians = math.radians(degrees)
        x_new = (self.x * math.cos(math_radians)
                 - self.y * math.sin(math_radians))
        y_new = (self.x * math.sin(math_radians)
                 + self.y * math.cos(math_radians))
        return Vector(x_new, y_new)
