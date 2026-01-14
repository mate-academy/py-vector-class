from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, param: float | int | Vector) -> Vector | float:
        if isinstance(param, (float, int)):
            return Vector(round(self.x * param, 2), round(self.y * param, 2))
        elif isinstance(param, Vector):
            return self.x * param.x + self.y * param.y
        else:
            raise TypeError("Parameter must be a float or Vector")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> Vector:
        first_point = end_point[0] - start_point[0]
        second_point = end_point[1] - start_point[1]
        return cls(first_point, second_point)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            return 0.0
        cos_angle = dot_product / (length_self * length_other)
        # Clamp value to avoid domain errors
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        if angle_degrees < 0:
            angle_degrees += 360
        return round(angle_degrees)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta
        return Vector(round(rotated_x, 2), round(rotated_y, 2))
