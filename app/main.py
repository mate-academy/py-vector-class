from __future__ import annotations
import math


class Vector:
    def __init__(self, x_asix: int | float, y_asix: int | float) -> None:
        self.x = round(x_asix, 2)
        self.y = round(y_asix, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_asix=self.x + other.x,
            y_asix=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_asix=self.x - other.x,
            y_asix=self.y - other.y,
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if not isinstance(other, Vector):
            return Vector(
                x_asix=round(self.x * other, 2),
                y_asix=round(self.y * other, 2)
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_asix=end_point[0] - start_point[0],
            y_asix=end_point[1] - start_point[1],
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_asix=self.x / self.get_length(),
            y_asix=self.y / self.get_length(),
        )

    def angle_between(self, other: Vector) -> int | float:
        return round((math.degrees
                      (math.acos((self * other)
                                 / (self.get_length()
                                    * math.sqrt(other.x ** 2 + other.y ** 2))
                                 )
                       )
                      )
                     )

    def get_angle(self) -> int | float:
        return round(math.atan2(-self.x, self.y) * 180 / math.pi)

    def rotate(self, other: int) -> Vector:
        return Vector(
            x_asix=((self.x * math.cos(math.radians(other)))
                    - (self.y * math.sin(math.radians(other)))),
            y_asix=((self.x * math.sin(math.radians(other)))
                    + (self.y * math.cos(math.radians(other))))
        )
