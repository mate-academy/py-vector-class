from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: int | float,
                 coordinate_y: int | float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other
            self.y += other

        return Vector(self.x, self.y)

    def __sub__(self, other: Vector | int | float) -> Vector:

        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y

        else:
            self.x -= other
            self.y -= other

        return Vector(self.x, self.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:

        if isinstance(other, Vector):
            self.x *= round(other.x, 2)
            self.y *= round(other.y, 2)
            return self.x + self.y

        else:
            self.x *= other
            self.y *= other
            return Vector(self.x, self.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:

        start = Vector(start_point[0], start_point[1])
        end = Vector(end_point[0], end_point[1])
        return cls.__sub__(end, start)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        coordinate_x = self.x / length
        coordinate_y = self.y / length
        return Vector(coordinate_x, coordinate_y)

    def angle_between(self, other: Vector) -> int | float:
        scalar = self.x * other.x + self.y * other.y
        multiplication =\
            math.sqrt(self.x ** 2 + self.y ** 2)\
            * math.sqrt(other.x ** 2 + other.y ** 2)
        result = scalar / multiplication
        return round(math.degrees(math.acos(result)))

    def get_angle(self) -> int | float:
        axis = Vector(0, 1)
        scalar = self.x * axis.x + self.y * axis.y
        multiplication =\
            math.sqrt(self.x ** 2 + self.y ** 2)\
            * math.sqrt(axis.x ** 2 + axis.y ** 2)
        result = scalar / multiplication
        return round(math.degrees(math.acos(result)))

    def rotate(self, degrees: int | float) -> Vector:
        degrees = math.radians(degrees)
        coordinate_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        coordinate_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(coordinate_x, coordinate_y)
