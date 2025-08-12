from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self,
                multiplier: int | float | Vector) \
            -> int | float | Vector:
        if isinstance(multiplier, Vector):
            return (self.x * multiplier.x
                    + self.y * multiplier.y)
        return Vector(self.x * multiplier,
                      self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        scalar_product = (self.x * other.x
                          + self.y * other.y)
        vectors_modules = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(
            scalar_product / vectors_modules
        )))

    def get_angle(self) -> int | float:
        scalar_product = self.y
        vectors_modules = self.get_length()
        return round(math.degrees(
            math.acos(scalar_product / vectors_modules)
        ))

    def rotate(self, angle: int | float) -> Vector:
        degrees_in_radians = math.radians(angle)
        x_value = (
            self.x * math.cos(degrees_in_radians)
            - self.y * math.sin(degrees_in_radians)
        )
        y_value = (
            self.x * math.sin(degrees_in_radians)
            + self.y * math.cos(degrees_in_radians)
        )
        return Vector(x_value, y_value)
