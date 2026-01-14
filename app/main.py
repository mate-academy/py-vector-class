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

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> float:
        return round(
            math.degrees(
                math.acos(
                    self * vector / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        angle_radians = abs(math.atan2(self.x, self.y))
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        return Vector(math.cos(math.radians(degrees))
                      * self.x - math.sin(math.radians(degrees))
                      * self.y,
                      math.sin(math.radians(degrees))
                      * self.x + math.cos(math.radians(degrees))
                      * self.y)
