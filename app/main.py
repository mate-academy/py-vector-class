from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return None

    def __sub__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return None

    def __mul__(self, other: int | float | Vector) -> Vector | float | None:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return None

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector | None:
        if (isinstance(start_point, tuple) and isinstance(end_point, tuple)
                and len(start_point) == 2 and len(end_point) == 2):
            return Vector(end_point[0] - start_point[0],
                          end_point[1] - start_point[1])
        return None

    def get_length(self) -> float:
        return (self.x * self.x + self.y * self.y) ** 0.5

    def get_normalized(self) -> Vector | None:
        vector_length = self.get_length()
        if vector_length:
            return Vector(self.x / vector_length, self.y / vector_length)
        return None

    def angle_between(self, other: Vector) -> float | None:
        self_length = self.get_length()
        if isinstance(other, Vector):
            other_length = other.get_length()
            if self_length and other_length:
                return round(math.degrees(math.acos(
                    (self * other) / (self_length * other_length))
                ))
        return None

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector | None:
        radians = math.radians(degrees)
        x_result = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_result = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_result, y_result)
