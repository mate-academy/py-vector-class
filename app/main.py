from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(x_coord=self.x * other, y_coord=self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        scale_factor = Vector.get_length(self)
        return Vector(
            x_coord=round((self.x / scale_factor), 2),
            y_coord=round((self.y / scale_factor), 2),
        )

    def angle_between(self, other: Vector) -> int:
        dot_prod = self.__mul__(other)
        length_first = self.get_length()
        length_second = other.get_length()
        cos = dot_prod / (length_first * length_second)
        return int(round(math.degrees(math.acos(cos)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(x_coord=0, y_coord=1))

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)
        old_x = self.x
        old_y = self.y
        self.x = old_x * math.cos(radians) - old_y * math.sin(radians)
        self.y = old_x * math.sin(radians) + old_y * math.cos(radians)

        return Vector(self.x, self.y)
