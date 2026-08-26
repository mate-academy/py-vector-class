from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: (int, float), y_cord: (int, float)) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):

            return Vector(
                x_cord=self.x + other.x,
                y_cord=self.y + other.y
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_cord=self.x - other.x,
                y_cord=self.y - other.y
            )

    def __mul__(self, other: (int, float, Vector)) -> (int, float):
        if isinstance(other, Vector):
            return round((self.x * other.x) + (self.y * other.y), 14)
        elif isinstance(other, (int, float)):
            return Vector(
                x_cord=self.x * other,
                y_cord=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point: (int, float),
                                    end_point: (int, float)) -> Vector:
        x_cord = end_point[0] - start_point[0]
        y_cord = end_point[1] - start_point[1]
        return cls(x_cord=x_cord, y_cord=y_cord)

    def get_length(self) -> (int, float):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(x_cord=0, y_cord=0)
        return Vector(
            x_cord=self.x / length,
            y_cord=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_a = dot_product / length_product
        cos_a = min(1, max(-1, cos_a))  # Ensure cos_a is within valid range
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        reference_vector = Vector(x_cord=0, y_cord=1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(
            x_cord=round(x_new, 2),
            y_cord=round(y_new, 2)
        )

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
