from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if type(other) == Vector:
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float],
                                    end_point: tuple[float]) -> Vector:
        return cls(x_coordinate=end_point[0] - start_point[0],
                   y_coordinate=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(x_coordinate=self.x / self.get_length(),
                      y_coordinate=self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_coordinate=round(self.x * math.cos(math.radians(degrees))
                               - self.y * math.sin(math.radians(degrees)), 2),
            y_coordinate=round(self.x * math.sin(math.radians(degrees))
                               + self.y * math.cos(math.radians(degrees)), 2))
