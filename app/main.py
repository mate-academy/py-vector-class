from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        else:
            raise TypeError

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        else:
            raise TypeError

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        raise TypeError

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate=x_coordinate, y_coordinate=y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)

        x_normalized = self.x / self.get_length()
        y_normalized = self.y / self.get_length()

        return Vector(x_normalized, y_normalized)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_theta = dot_product / (length_self * length_other)
        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> float:
        length_self = self.get_length()
        cos_theta = self.y / length_self
        angle_radians = math.acos(cos_theta)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)
