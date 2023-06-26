from __future__ import annotations
from math import degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            coordinate_x=end_point[0] - start_point[0],
            coordinate_y=end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            coordinate_x=round(self.x / length, 2),
            coordinate_y=round(self.y / length, 2),
        )

    def angle_between(self, other_vector: Vector) -> int:
        cos_a = ((self
                 * other_vector)
                 * (1
                    / (self.get_length()
                        * other_vector.get_length())))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degrees: int) -> Vector:
        cos_a = cos(radians(degrees))
        sin_a = sin(radians(degrees))
        return Vector(
            coordinate_x=(self.x * cos_a - self.y * sin_a),
            coordinate_y=(self.y * cos_a + self.x * sin_a)
        )
