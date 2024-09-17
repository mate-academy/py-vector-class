from __future__ import annotations
import math


class Vector:
    def __init__(self, cord_x: int | float, cord_y: int | float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(math.acos((self.x * other.x + self.y * other.y) / (
                ((self.x ** 2 + self.y ** 2) ** 0.5) * (
                    (other.x ** 2 + other.y ** 2) ** 0.5)))))

    def get_angle(self) -> int | float:
        return round(math.degrees(math.acos(self.y / (
            (self.x ** 2 + self.y ** 2) ** 0.5))))

    def rotate(self, degree: int) -> Vector:
        rotated_x = (
            self.x * math.cos(math.radians(degree)) - (
                self.y * math.sin(math.radians(degree))))
        rotated_y = (
            self.x * math.sin(math.radians(degree)) + (
                self.y * math.cos(math.radians(degree))))
        return Vector(rotated_x, rotated_y)
