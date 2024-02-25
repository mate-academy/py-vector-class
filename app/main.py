from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / Vector.get_length(self),
                      self.y / Vector.get_length(self))

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other)
                    / (Vector.get_length(self)
                       * Vector.get_length(other))
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            math.cos(degrees) * self.x - math.sin(degrees) * self.y,
            math.sin(degrees) * self.x + math.cos(degrees) * self.y
        )
