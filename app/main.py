from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float | int, y_cord: float | int) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_cord=self.x + other.x,
            y_cord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float | int:
        return math.sqrt(self.y ** 2 + self.x ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length1 = self.get_length()
        length2 = other.get_length()
        cos_a = dot_product / (length1 * length2)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector | float:
        radians = math.radians(degrees)
        rotated_x = (self.x * math.cos(radians) - self.y * math.sin(radians))
        rotated_y = (self.x * math.sin(radians) + self.y * math.cos(radians))
        return Vector(rotated_x, rotated_y)
