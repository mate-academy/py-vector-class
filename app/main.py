from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x += other.x
        self.x = round(self.x, 2)
        self.y += other.y
        self.y = round(self.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x -= other.x
        self.y -= other.y
        self.x = round(self.x, 2)
        self.y = round(self.y, 2)
        return self

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            self.x = round(self.x, 2)
            self.y = round(self.y, 2)
            return self
        dot_product = (self.x * other.x + self.y * other.y)
        return dot_product

    @classmethod
    def create_vector_by_two_points(cls, first_point: tuple,
                                    second_point: tuple) -> Vector:
        x_difference = second_point[0] - first_point[0]
        y_difference = second_point[1] - first_point[1]
        return cls(x_difference, y_difference)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length_of_vector = self.get_length()
        inverse_length = 1 / length_of_vector
        return Vector(self.x * inverse_length, self.y * inverse_length)

    def angle_between(self, other: Vector) -> int | float:
        dot_product = (self.x * other.x + self.y * other.y)
        magnitudes = (((self.x ** 2 + self.y ** 2) ** 0.5)
                      * ((other.x ** 2 + other.y ** 2) ** 0.5))
        cos_theta = dot_product / magnitudes
        angle_in_radians = math.acos(cos_theta)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        angle_in_radians = math.atan2(self.x, self.y)
        angle_in_degrees = math.degrees(angle_in_radians)
        angle_in_degrees = round(angle_in_degrees * -1)
        return angle_in_degrees

    def rotate(self, angle_deg: float) -> Vector:
        # Convert the angle to radians
        angle_rad = math.radians(angle_deg)

        # Calculate new coordinates after rotation
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)

        # Update the vector's coordinates
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)
        return self
