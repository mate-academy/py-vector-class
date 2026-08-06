from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coor: int | float, y_ccor: int | float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_ccor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[int | float],
                                    end_point: tuple[int | float]) -> Vector:
        return Vector((end_point[0] - start_point[0]),
                      (end_point[1] - start_point[1]))

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(self.__mul__(other)
                                            / (self.get_length()
                                               * other.get_length()))))

    def get_angle(self) -> int | float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
