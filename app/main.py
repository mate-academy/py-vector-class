from __future__ import annotations
import math


class Vector:

    def __init__(self, v_x: float, v_y: float) -> None:
        self.v_x = round(v_x, 2)
        self.v_y = round(v_y, 2)

    @property
    def x(self) -> float:
        return self.v_x

    @property
    def y(self) -> float:
        return self.v_y

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point : tuple,
            end_point : tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = round(self.get_length(), 2)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        scalar_prod = self.x * other.x + self.y * other.y
        cos_a = scalar_prod / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
