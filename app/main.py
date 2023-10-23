from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round((self.x * other), 2), round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:

        start_point = list(start_point)
        end_point = list(end_point)

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        numerator = self.x * other.x + self.y * other.y
        denominator = ((self.x**2 + self.y**2)**0.5
                       * (other.x**2 + other.y**2)**0.5)

        return round(math.degrees(math.acos(numerator / denominator)))

    def get_angle(self) -> int | float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        x_var = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_var = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(x_var, y_var)
