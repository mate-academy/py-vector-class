from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length,
                      self.y * inv_length)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            self * other
            / (self.get_length() * other.get_length())))
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: float) -> Vector:
        rotated_x = round(self.x * math.cos(math.radians(angle))
                          - self.y * math.sin(math.radians(angle)), 2)
        rotated_y = round(self.x * math.sin(math.radians(angle))
                          + self.y * math.cos(math.radians(angle)), 2)
        return Vector(rotated_x, rotated_y)
