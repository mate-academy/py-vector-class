from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector | str:
        if not isinstance(other, Vector):
            return f"{other} instance is not the instance of the Vector Class!"
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector | str:
        if not isinstance(other, Vector):
            return f"{other} instance is not the instance of the Vector Class!"
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        self_magnitude = self.get_length()
        other_magnitude = other.get_length()
        cos_theta = dot_product / (self_magnitude * other_magnitude)
        angle_theta_rad = math.acos(cos_theta)
        angle_theta_deg = round(math.degrees(angle_theta_rad))
        return angle_theta_deg

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degrees: int) -> Vector:
        angle_in_rad = math.radians(degrees)
        x2 = math.cos(angle_in_rad) * self.x - math.sin(angle_in_rad) * self.y
        y2 = math.sin(angle_in_rad) * self.x + math.cos(angle_in_rad) * self.y
        return Vector(x2, y2)
