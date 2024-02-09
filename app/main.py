from __future__ import annotations
from math import sqrt, acos, degrees, ceil, radians, cos, sin


class Vector:

    def __init__(self,
                 x_coordinate: int | float,
                 y_coordinate: int | float
                 ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> float | int | Vector:
        if not isinstance(other, Vector):
            return Vector(
                self.x * other,
                self.y * other
            )
        return (self.x * other.x) + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple,
    ) -> Vector:
        return Vector(
            x_coordinate=end_point[0] - start_point[0],
            y_coordinate=end_point[1] - start_point[1],
        )

    def get_length(self) -> int | float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> None:
        length_of_vector = self.get_length()
        return Vector(
            x_coordinate=self.x / length_of_vector,
            y_coordinate=self.y / length_of_vector
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_v = sqrt(self.x ** 2 + self.y ** 2)
        magnitude_u = sqrt(other.x ** 2 + other.y ** 2)
        angle_radians = acos(dot_product / (magnitude_v * magnitude_u))
        angle_degrees = degrees(angle_radians)
        return ceil(angle_degrees)

    def get_angle(self) -> int:
        angle_between_current_v = degrees(
            acos(self.y / self.get_length())
        )
        return round(angle_between_current_v)

    def rotate(self, value: int) -> float:
        angle_radians = radians(value)
        cos_theta = cos(angle_radians)
        sin_theta = sin(angle_radians)
        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta
        return Vector(x_coordinate=rotated_x, y_coordinate=rotated_y)
