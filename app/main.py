from __future__ import annotations
import math


class Vector:
    def __init__(self, x_sms: float, y_sms: float) -> None:
        self.x = round(x_sms, 2)
        self.y = round(y_sms, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        return (
            cls(
                end_point[0] - start_point[0],
                end_point[1] - start_point[1]
            )
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        vectors_mul = self * other
        vectors_length_mul = self.get_length() * other.get_length()
        cos_a = vectors_mul / vectors_length_mul
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x2 = math.cos(radians) * self.x - math.sin(radians) * self.y
        y2 = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(x2, y2)
