from __future__ import annotations
from math import sqrt, acos, degrees
from math import sin, cos, radians


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, multiplier: int | float | Vector) -> Vector | float:
        if isinstance(multiplier, (int, float)):
            return Vector(round(self.x * multiplier, 2),
                          round(self.y * multiplier, 2))
        if isinstance(multiplier, Vector):
            return Vector.multiplie_two_vectors(self, multiplier)
        return NotImplemented

    @staticmethod
    def multiplie_two_vectors(vector_a: Vector, vector_b: Vector) -> float:
        return vector_a.x * vector_b.x + vector_a.y * vector_b.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple,
                                    end: tuple) -> Vector:

        start_type = all(isinstance(coord, (int, float)) for coord in start)
        end_type = all(isinstance(coord, (int, float)) for coord in end)

        if len(start) > 1 and len(end) > 1 and start_type and end_type:
            return cls(end[0] - start[0], end[1] - start[1])
        return NotImplemented

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> float:
        if isinstance(other, Vector):
            multiplied_vectors = Vector.multiplie_two_vectors(self, other)
            multiplied_lenghts = (self.get_length() * other.get_length())
            cosinus = multiplied_vectors / multiplied_lenghts
            return round(degrees(acos(cosinus)), 0)
        return NotImplemented

    def get_angle(self) -> float:
        return round(degrees(acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        radian = radians(degrees)
        x_axis = cos(radian) * self.x - sin(radian) * self.y
        y_axis = sin(radian) * self.x + cos(radian) * self.y
        return Vector(x_axis, y_axis)
