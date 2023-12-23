from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coo: float, y_coo: float) -> None:
        self.x = round(x_coo, 2)
        self.y = round(y_coo, 2)

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

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other
        )

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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self.__mul__(vector)
                 / (self.get_length() * vector.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            (self.x * math.cos(math.radians(degrees))
             - self.y * math.sin(math.radians(degrees))),
            (self.x * math.sin(math.radians(degrees))
             + self.y * math.cos(math.radians(degrees)))
        )
