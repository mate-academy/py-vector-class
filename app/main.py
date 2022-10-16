from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> object:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> object:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: float) -> object:
        if isinstance(other, (float, int)):
            return Vector((self.x * other), (self.y * other))
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        return Vector((self.x / self.get_length()),
                      (self.y / self.get_length()))

    def angle_between(self, other: Vector) -> float:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> object:
        point_x = (math.cos(math.radians(degrees)) * self.x) - \
                  (math.sin(math.radians(degrees)) * self.y)
        point_x = (math.sin(math.radians(degrees)) * self.x) + \
                  (math.cos(math.radians(degrees)) * self.y)
        return Vector(point_x, point_x)
