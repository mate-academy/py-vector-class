from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, new: Vector) -> Vector:
        return Vector(self.x + new.x, self.y + new.y)

    def __sub__(self, new: Vector) -> Vector:
        return Vector(self.x - new.x, self.y - new.y)

    def __mul__(self, new: int | float | Vector) -> Vector | int | float:
        if isinstance(new, int | float):
            return Vector(self.x * new, self.y * new)
        return self.x * new.x + self.y * new.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return abs(
            (self.x ** 2 + self.y ** 2) ** 0.5
        )

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(), self.y / self.get_length()
        )

    def angle_between(self, new: Vector) -> int:
        a_cos = math.acos(
            self.__mul__(new) / (self.get_length() * new.get_length())
        )
        return round(math.degrees(a_cos))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int | float) -> Vector:
        rad = math.radians(degrees)
        new_x = math.cos(rad) * self.x - math.sin(rad) * self.y
        new_y = math.sin(rad) * self.x + math.cos(rad) * self.y
        return Vector(new_x, new_y)
