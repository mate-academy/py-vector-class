from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

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

    def __mul__(self, other: Vector) -> (Vector, int, float):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> (int, float):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        angle_cos = ((Vector.__mul__(self, other))
                     / (Vector.get_length(self)
                        * (Vector.get_length(other))))
        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self) -> int:
        angle_cos = self.y / Vector.get_length(self)
        return round(math.degrees(math.acos(angle_cos)))

    def rotate(self, degrees: int) -> Vector:
        rad_degrees = math.radians(degrees)
        return Vector(
            math.cos(rad_degrees) * self.x - math.sin(rad_degrees) * self.y,
            math.sin(rad_degrees) * self.x + math.cos(rad_degrees) * self.y
        )
