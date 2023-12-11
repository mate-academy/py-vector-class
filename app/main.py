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

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector((self.x / (self.x ** 2 + self.y ** 2) ** 0.5),
                      (self.y / (self.x ** 2 + self.y ** 2) ** 0.5))

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            (self.x * other.x + self.y * other.y)
            / (((self.x ** 2 + self.y ** 2) ** 0.5)
               * (other.x ** 2 + other.y ** 2) ** 0.5))))

    def get_angle(self) -> int:
        if self.x < 0 and self.y < 0:
            return round(180
                         - (math.degrees
                            (math.acos((self.x * 0 + self.y * self.y)
                                       / (((self.x ** 2 + self.y ** 2) ** 0.5)
                                          * ((self.x ** 2 + self.y ** 2)
                                             - self.x ** 2) ** 0.5)))))
        return round(math.degrees
                     (math.acos((self.x * 0 + self.y * self.y)
                                / (((self.x ** 2 + self.y ** 2) ** 0.5)
                                   * ((self.x ** 2 + self.y ** 2)
                                      - self.x ** 2) ** 0.5))))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,
            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y)
