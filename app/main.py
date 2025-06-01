from __future__ import annotations
from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y
                      )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y
                      )

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, Vector):
            return ((self.x * other.x)
                    + (self.y * other.y)
                    )
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1]
                   )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length,
                      self.y / length
                      )

    def angle_between(self, other: Vector) -> float:
        return round(degrees(acos((self * other)
                                  / (self.get_length() * other.get_length())))
                     )

    def get_angle(self) -> float:
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        degree = radians(degree)
        return Vector(cos(degree) * self.x - sin(degree) * self.y,
                      sin(degree) * self.x + cos(degree) * self.y
                      )
