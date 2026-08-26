from __future__ import annotations

from math import sqrt, cos, acos, degrees, sin, radians


class Vector:
    def __init__(self, some_x: float, some_y: float) -> None:
        self.x = round(some_x, 2)
        self.y = round(some_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"{type(other)} not a Vector")
        res_x = self.x + other.x
        res_y = self.y + other.y
        return Vector(res_x, res_y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"{type(other)} not a Vector")
        res_x = self.x - other.x
        res_y = self.y - other.y
        return Vector(res_x, res_y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            res_x = self.x * other.x
            res_y = self.y * other.y
            return res_x + res_y
        res_x = self.x * other
        res_y = self.y * other
        return Vector(res_x, res_y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        # Returns length of the vector.
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        # Returns normalized copy of vector.
        # Normalized vector has length = 1
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, vector: Vector) -> int:
        # Returns angle between current vector and vector in integer degrees.
        scalar_mult = self * vector
        vector_mult = self.get_length() * vector.get_length()
        cos_a = scalar_mult / vector_mult
        alpha = degrees(acos(cos_a))
        return round(alpha)

    def get_angle(self) -> int:
        # Returns angle between current vector and positive Y axis.
        axis_y = Vector(0, 1)
        angle = self.angle_between(axis_y)
        return round(angle, 2)

    def rotate(self, degrees: int) -> Vector:
        # Returns rotated Vector by degrees.
        # Theory:
        # x' = x*cos_fi - y*sin_fi
        # y′ = x*sin_fi + y*cos_fi
        rad_degrees = radians(degrees)
        new_x = self.x * cos(rad_degrees) - self.y * sin(rad_degrees)
        new_y = self.x * sin(rad_degrees) + self.y * cos(rad_degrees)
        return Vector(new_x, new_y)
