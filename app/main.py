from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise ValueError(f"Unsupported type for +: {type(other)}")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise ValueError(f"Unsupported type for -: {type(other)}")

    def __mul__(
            self, other: Vector | int | float
    ) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise ValueError(f"Unsupported type for *: {type(other)}")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return cls(point_x, point_y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        if isinstance(vector, Vector):
            dot_product = self * vector
            len_self = self.get_length()
            len_other = vector.get_length()
            if len_self == 0 or len_other == 0:
                raise ValueError(
                    "Cannot compute angle with zero-length vector"
                )
            cos_a = dot_product / (len_self * len_other)
            cos_a = max(-1, min(1, cos_a))
            return round(math.degrees(math.acos(cos_a)))
        raise ValueError(f"Unsupported type of vector: {type(vector)}")

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        if angle < 0:
            angle += 360
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = round(self.x * cos_theta - self.y * sin_theta, 2)
        new_y = round(self.x * sin_theta + self.y * cos_theta, 2)
        return Vector(new_x, new_y)
