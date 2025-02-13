from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: (int, float), y_coord: (int, float)) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: (int, float)) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other , self.y + other)

    def __sub__(self, other: (int, float)) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other , self.y - other)

    def __mul__(self, other: (int, float)) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: (int, float)) -> float:
        if isinstance(other, Vector):

            magnitude_self = math.sqrt(self.x ** 2 + self.y ** 2)
            magnitude_other = math.sqrt(other.x ** 2 + other.y ** 2)
            cos_theta = ((self.x * other.x + self.y * other.y)
                         / (magnitude_self * magnitude_other))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int | float:
        angle = math.degrees(math.atan2(self.x, self.y))

        return (round(angle) ** 2) ** 0.5

    def rotate(self, degrees: (int, float)) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        return Vector(
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta
        )
