from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ValueError(
                "Cannot calculate angle with a zero-length vector."
            )

        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))

        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)

        return int(round(angle_degrees))

    def get_angle(self) -> int:
        angle = round(math.degrees(math.atan2(self.x, self.y)))
        if angle < 0:
            angle *= -1
        return angle

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
