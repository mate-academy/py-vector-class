from __future__ import annotations
import math


class Vector:

    def __init__(
            self, x_coordinate: int | float,
            y_coordinate: int | float
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, new_vector: Vector) -> Vector:
        return Vector(
            round(self.x + new_vector.x, 2),
            round(self.y + new_vector.y, 2)
        )

    def __sub__(self, new_vector: Vector) -> Vector:
        return Vector(
            round(self.x - new_vector.x, 2),
            round(self.y - new_vector.y, 2)
        )

    def __mul__(self, new_vector: Vector | int | float) -> int | Vector:
        if isinstance(new_vector, (int, float)):
            return Vector(
                round(self.x * new_vector, 2),
                round(self.y * new_vector, 2)
            )
        return self.x * new_vector.x + self.y * new_vector.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_start, x_end = start_point
        y_start, y_end = end_point
        return cls(round(y_start - x_start, 2), round(y_end - x_end, 2))

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> float:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, new_vector: Vector) -> float:
        dot_product = self * new_vector
        length_self = self.get_length()
        length_other = new_vector.get_length()

        cos_theta = dot_product / (length_self * length_other)

        theta_radians = math.acos(cos_theta)

        theta_degrees = math.degrees(theta_radians)

        return round(theta_degrees)

    def get_angle(self) -> float:
        dot_product = self.y
        length_self = self.get_length()

        cos_theta = dot_product / length_self

        theta_radians = math.acos(cos_theta)

        theta_degrees = math.degrees(theta_radians)

        return round(theta_degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = round(
            self.x * math.cos(radians) - self.y * math.sin(radians), 2
        )
        new_y = round(
            self.x * math.sin(radians) + self.y * math.cos(radians), 2
        )

        return Vector(new_x, new_y)
