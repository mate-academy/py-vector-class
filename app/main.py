from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)
        raise TypeError(
            "Unsupported type to subtraction"
        )

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            mul_x = self.x * other.x
            mul_y = self.y * other.y
            return mul_x + mul_y
        raise TypeError("Must be (int|float) or cls type")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        new_point_x = end_point[0] - start_point[0]
        new_point_y = end_point[1] - start_point[1]
        return cls(new_point_x, new_point_y)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            scalar = self * other
            mul_of_length = self.get_length() * other.get_length()
            result = math.degrees(math.acos(scalar / mul_of_length))
            return round(result)
        raise TypeError("Unsupported type")

    def get_angle(self) -> int | float:
        axis_y = Vector(0, 1)
        return self.angle_between(axis_y)

    def rotate(self, angle: int) -> Vector:
        x_a = (self.x * math.cos(math.radians(angle))
               - self.y * math.sin(math.radians(angle)))
        y_a = (self.x * math.sin(math.radians(angle))
               + self.y * math.cos(math.radians(angle)))
        return Vector(round(x_a, 2), round(y_a, 2))
