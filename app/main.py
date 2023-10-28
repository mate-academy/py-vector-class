from __future__ import annotations
from math import acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" | float) -> "Vector" | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        magnitude = (self.x ** 2 + self.y ** 2) ** 0.5
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, other: "Vector") -> float:
        magnitude_self = (self.x**2 + self.y**2) ** 0.5
        magnitude_other = (other.x ** 2 + other.y ** 2) ** 0.5
        dot_product = self.x * other.x + self.y * other.y

        cos_theta = dot_product / (magnitude_self * magnitude_other)

        cos_theta = max(-1.0, min(1.0, cos_theta))
        theta = acos(cos_theta)

        return round(degrees(theta))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 10))

    def rotate(self, dgrees: int) -> "Vector":
        theta = radians(dgrees)

        x_new = self.x * cos(theta) - self.y * sin(theta)
        y_new = self.x * sin(theta) + self.y * cos(theta)

        return Vector(round(x_new, 2), round(y_new, 2))
