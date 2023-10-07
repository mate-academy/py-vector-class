from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other,
                      y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = Vector.__mul__(self, other)
        cosine_theta = dot_product / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(cosine_theta))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rads = math.radians(degrees)
        x_new = self.x * math.cos(rads) - self.y * math.sin(rads)
        y_new = self.x * math.sin(rads) + self.y * math.cos(rads)
        return Vector(x=x_new, y=y_new)
