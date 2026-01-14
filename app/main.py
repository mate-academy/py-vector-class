from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    # def dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(round(normalized_x, 2), round(normalized_y, 2))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        return abs(round(math.degrees(angle_radians)))

    def angle_between(self, other: Vector) -> int:
        angle = math.acos((self.x * other.x + self.y * other.y)
                          / ((math.sqrt(self.x ** 2 + self.y ** 2))
                          * math.sqrt(other.x ** 2 + other.y ** 2)))
        return round(math.degrees(angle))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
