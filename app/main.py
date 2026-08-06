from __future__ import annotations
import math


class Vector:
    def __init__(self, x_number: float, y_number: float) -> None:
        self.x = round(x_number, 2)
        self.y = round(y_number, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        return self.x * other.x + self.y * other.y \
            if isinstance(other, Vector) \
            else Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1]
                      )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return math.ceil(math.degrees(math.acos(self.get_normalized()
                                                * other.get_normalized())))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(round(self.x * math.cos(radians)
                            - self.y * math.sin(radians), 2),
                      round(self.x * math.sin(radians)
                            + self.y * math.cos(radians), 2))
