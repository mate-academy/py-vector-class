from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(float(x), 2)
        self.y = round(float(y), 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> Vector:
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        lengths_multiplied = self.get_length() * other.get_length()

        if lengths_multiplied == 0:
            return 0

        cos_a = dot_product / lengths_multiplied

        cos_a = max(-1.0, min(1.0, cos_a))

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)

        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)

        return Vector(new_x, new_y)
