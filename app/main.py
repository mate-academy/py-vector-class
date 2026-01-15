from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=(self.x + other.x),
            coord_y=(self.y + other.y),
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=(self.x - other.x),
            coord_y=(self.y - other.y),
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(coord_x=self.x * other, coord_y=self.y * other, )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector((end_point[0] - start_point[0]),
                      (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length(),
        )

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self.__mul__(vector)
                 / (self.get_length() * vector.get_length()))
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        axis_y = Vector(0, 1)
        return self.angle_between(axis_y)

    def rotate(self, degrees: int) -> Vector:
        rad_degree = math.radians(degrees)
        return Vector(math.cos(rad_degree) * self.x
                      - math.sin(rad_degree) * self.y,
                      math.sin(rad_degree) * self.x
                      + math.cos(rad_degree) * self.y,)
