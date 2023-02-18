from __future__ import annotations
import math
import numpy


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return numpy.dot([self.x, self.y], [other.x, other.y])
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector = [self.x, self.y]
        unit_vector = vector / numpy.linalg.norm(vector)
        return Vector(round(unit_vector[0], 2), round(unit_vector[1], 2))

    def angle_between(self, other: Vector) -> int:
        result = numpy.dot(self, other) / (Vector.get_length(self)
                                           * Vector.get_length(other))
        return round(math.degrees(math.acos(result)))

    def get_angle(self) -> int:
        vector = [self.x, self.y]
        y_axis = [0, 1]
        unit_vector = vector / numpy.linalg.norm(vector)
        unit_y = y_axis / numpy.linalg.norm(y_axis)
        dot_product = numpy.dot(unit_vector, unit_y)
        angle = numpy.arccos(dot_product)
        return round(360 * angle / (2 * numpy.pi))

    def rotate(self, degrees: int) -> Vector:
        coord_x = self.x
        coord_y = self.y
        angle = math.radians(degrees)
        xr = coord_x * math.cos(angle) - coord_y * math.sin(angle)
        yr = coord_x * math.sin(angle) + coord_y * math.cos(angle)
        return Vector(xr, yr)
