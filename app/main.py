from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_component: int | float,
            y_component: int | float
    ) -> None:
        self.x = round(x_component, 2)
        self.y = round(y_component, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (
            (self.x * other.x + self.y * other.y)
            / (self.get_length() * other.get_length())
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, other: int) -> Vector:
        angle = math.radians(other)  # Convert degrees to radians
        sin_theta = math.sin(angle)
        cos_theta = math.cos(angle)
        x_prime = self.x * cos_theta - self.y * sin_theta
        y_prime = self.x * sin_theta + self.y * cos_theta
        return Vector(x_prime, y_prime)
