from __future__ import annotations

import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("argument should be a Vector instance")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("argument should be a Vector instance")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Vector | int | float
    ) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("argument should be a Vector "
                            "instance or a number (int or float)")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Zero-length vector cannot be normalized")
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ValueError("Cannot calculate the "
                             "angle with a zero-length vector")

        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_radians = math.acos(cos_theta)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> int:
        axis_y = Vector(0, 1)
        dot_product = self.x * axis_y.x + self.y * axis_y.y
        length_self = self.get_length()
        length_axis_y = axis_y.get_length()

        if length_self == 0:
            raise ValueError("Cannot calculate angle for zero-length vector")

        cos_theta = dot_product / (length_self * length_axis_y)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)

        if angle_degrees < 0:
            angle_degrees += 360

        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta

        rotated_x = round(rotated_x, 2)
        rotated_y = round(rotated_y, 2)

        return Vector(rotated_x, rotated_y)
