from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other,
                      y=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x_coor = end_point[0] - start_point[0]
        y_coor = end_point[1] - start_point[1]
        return cls(x_coor, y_coor)

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other_vector: Vector) -> float:
        doubled_x = self.x * other_vector.x
        doubled_y = self.y * other_vector.y
        dot_product = doubled_x + doubled_y
        magnitude_product = self.get_length() * other_vector.get_length()
        angle_radians = math.acos(dot_product / magnitude_product)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        dot_product = self * y_axis
        self_magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        y_axis_magnitude = math.sqrt(y_axis.x ** 2 + y_axis.y ** 2)
        cos_a = dot_product / (self_magnitude * y_axis_magnitude)
        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: float) -> Vector:
        angle_radians = math.radians(degrees)
        x_cos = self.x * math.cos(angle_radians)
        y_cos = self.y * math.sin(angle_radians)
        new_x = x_cos - y_cos
        x_sin = self.x * math.sin(angle_radians)
        y_cos = self.y * math.cos(angle_radians)
        new_y = x_sin + y_cos
        return Vector(new_x, new_y)
