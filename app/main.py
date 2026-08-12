from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = Vector.get_length(self)
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        angle_cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self) -> int:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        degrees_in_radians = math.radians(degrees)
        new_x = (self.x * math.cos(degrees_in_radians)
                 - self.y * math.sin(degrees_in_radians))
        new_y = (self.x * math.sin(degrees_in_radians)
                 + self.y * math.cos(degrees_in_radians))
        return Vector(new_x, new_y)
