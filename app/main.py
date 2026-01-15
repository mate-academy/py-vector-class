from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)
        self.x = self.x_coordinate
        self.y = self.y_coordinate

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_coordinate + other.x_coordinate,
                      self.y_coordinate + other.y_coordinate)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x_coordinate - other.x_coordinate,
                      self.y_coordinate - other.y_coordinate)

    def __mul__(self, other: float | int | Vector) -> Vector | None | float:
        if isinstance(other, float | int):
            return Vector(self.x_coordinate * other,
                          self.y_coordinate * other)
        if isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate
                    + self.y_coordinate * other.y_coordinate)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[int | float],
                                    end_point: tuple[int | float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt(self.x_coordinate ** 2 + self.y_coordinate ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x_coordinate / self.get_length(),
                      self.y_coordinate / self.get_length())

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length())
        )), 0)

    def get_angle(self) -> float | int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            self.x_coordinate * math.cos(radians)
            - self.y_coordinate * math.sin(radians),
            self.x_coordinate * math.sin(radians)
            + self.y_coordinate * math.cos(radians)
        )
