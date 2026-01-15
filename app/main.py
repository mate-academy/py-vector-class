from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: [float, int], y_coord: [float, int]) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: [Vector, int, float]) -> [Vector, int, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other
        )

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x * 1 / self.get_length(), self.y * 1 / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        mul = self * other
        length = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(mul / length)))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        return Vector(
            x_coord=cos * self.x - sin * self.y,
            y_coord=sin * self.x + cos * self.y
        )

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return round(
            math.degrees(
                math.acos(
                    self * y_axis / (self.get_length() * y_axis.get_length())
                )
            )
        )
