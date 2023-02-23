from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float | int, y_point: float | int) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

        return Vector(round((self.x * other), 2), round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        x_new = round((self.x / self.get_length()), 2)
        y_new = round((self.y / self.get_length()), 2)
        return Vector(x_new, y_new)

    def angle_between(self, other: Vector) -> int:
        cos = ((self.x * other.x + self.y * other.y)
               / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        y_axis = (0, 1)  # x == 0, y == 1
        len_y_axis = 1
        cos = ((self.x * y_axis[0] + self.y * y_axis[1])
               / (self.get_length() * len_y_axis))
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees: int) -> Vector:
        x_new = round((math.cos(math.radians(degrees)) * self.x)
                      - (math.sin(math.radians(degrees)) * self.y), 2)
        y_new = round((math.sin(math.radians(degrees)) * self.x)
                      + (math.cos(math.radians(degrees)) * self.y), 2)
        return Vector(x_new, y_new)
