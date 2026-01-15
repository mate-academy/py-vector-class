from __future__ import annotations
from math import sqrt, degrees, acos, atan2, radians, cos, sin


class Vector:
    def __init__(self, axis_x: float, axis_y: float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / self.get_length(),
                          self.y / self.get_length())

    def angle_between(self, other_vector: Vector) -> int:
        dot = self * other_vector
        length = self.get_length() * other_vector.get_length()
        cos_theta = min(max(dot / length, -1), 1)
        return round(degrees(acos(cos_theta)))

    def get_angle(self) -> int:
        return abs(round(degrees(atan2(self.x, self.y))))

    def rotate(self, add_degrees: int) -> Vector:
        degrees_to_radians = radians(add_degrees)
        cos_theta = cos(degrees_to_radians)
        sin_theta = sin(degrees_to_radians)
        rotated_x = self.x * cos_theta - self.y * sin_theta
        rotated_y = self.x * sin_theta + self.y * cos_theta
        return Vector(rotated_x, rotated_y)
