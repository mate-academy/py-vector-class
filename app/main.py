from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        mul = self.x * other.x + self.y * other.y
        length1 = (self.x ** 2 + self.y ** 2) ** 0.5
        length2 = (other.x ** 2 + other.y ** 2) ** 0.5
        angle_r = math.acos(mul / (length1 * length2))
        return round(math.degrees(angle_r))

    def get_angle(self) -> int:
        mul = self.x * 0 + self.y * 1
        length1 = (self.x ** 2 + self.y ** 2) ** 0.5
        length2 = (0 ** 2 + 1 ** 2) ** 0.5
        angle_r = math.acos(mul / (length1 * length2))
        return round(math.degrees(angle_r))

    def rotate(self, degree: int) -> Vector:
        angle_in_radians = math.radians(degree)
        new_x = self.x * math.cos(angle_in_radians) \
            - self.y * math.sin(angle_in_radians)
        new_y = self.x * math.sin(angle_in_radians) \
            + self.y * math.cos(angle_in_radians)
        return Vector(new_x, new_y)
