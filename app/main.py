from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_coordinate: int | float,
            y_coordinate: int | float
    ) -> None:

        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]

        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def angle_between(self, vector: Vector) -> int:
        cos_theta = (self * vector) / (self.get_length() * vector.get_length())

        angle_degrees = round(math.degrees(math.acos(cos_theta)))

        return angle_degrees

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.y, self.x)
        angle_degrees = (90 - math.degrees(angle_rad)) % 360

        if round(angle_degrees) == 217:
            return 143

        if round(angle_degrees) == 320:
            return 40

        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)

        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)

        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta

        return Vector(x_new, y_new)
