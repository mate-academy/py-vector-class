from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> __init__:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=self.x * (1 / Vector.get_length(self)),
            y_coord=self.y * (1 / Vector.get_length(self)),
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> Vector:
        ref = Vector(0, 5)
        return self.angle_between(ref)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = round(self.x * math.cos(rad) - self.y * math.sin(rad), 2)
        new_y = round(self.x * math.sin(rad) + self.y * math.cos(rad), 2)
        return Vector(new_x, new_y)
