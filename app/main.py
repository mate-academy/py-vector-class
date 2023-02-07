from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)
        self.params = (self.x, self.y)

    def __add__(self, other: Vector) -> Vector:
        return Vector(*[x + y for x, y in zip(self.params, other.params)])

    def __sub__(self, other: Vector) -> Vector:
        return Vector(*[x - y for x, y in zip(self.params, other.params)])

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        return sum([x * y for x, y in zip(self.params, other.params)])

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        vector = object.__new__(cls)
        start_x, start_y = start_point
        end_x, end_y = end_point
        vector.x = round(end_x - start_x, 2)
        vector.y = round(end_y - start_y, 2)
        vector.params = (vector.x, vector.y)
        return vector

    def get_length(self) -> float:
        return sum([param**2 for param in self.params]) ** 0.5

    def get_normalized(self) -> Vector:
        new_x = self.x / (self.x * self.x + self.y * self.y) ** 0.5
        new_y = self.y / (self.x * self.x + self.y * self.y) ** 0.5
        return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> int:
        mod_vector_1 = (self.x**2 + self.y**2) ** 0.5
        mod_vector_2 = (other.x**2 + other.y**2) ** 0.5
        mod_vector = mod_vector_2 * mod_vector_1
        return round(math.degrees(math.acos(self.__mul__(other) / mod_vector)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        new_x = (
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y
        )
        new_y = (
            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y
        )
        return Vector(new_x, new_y)
