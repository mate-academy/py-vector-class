from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        dot_product = self.x * vector.x + self.y * vector.y
        mod_vector = math.sqrt(self.x ** 2 + self.y ** 2) \
            * math.sqrt(vector.x ** 2 + vector.y ** 2)
        return math.ceil(math.degrees(math.acos(dot_product / mod_vector)))

    def get_angle(self) -> int:
        if self.x == 0:
            return 0
        return self.angle_between(Vector(0, 1)) - 1

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
