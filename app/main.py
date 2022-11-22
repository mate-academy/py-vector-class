from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x + other.x,
            y_point=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x - other.x,
            y_point=self.y - other.y,
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if other == 0:
            return Vector(x_point=0, y_point=0)
        if isinstance(other, float):
            return Vector(
                x_point=self.x * other,
                y_point=self.y * other,
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple,
    ) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(x_point=cls.x, y_point=cls.y)

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if not length:
            return self
        return Vector(x_point=self.x / length, y_point=self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            self.__mul__(other) / (self.get_length() * other.get_length()),
        )))

    def get_angle(self) -> int:
        other = Vector(x_point=0, y_point=abs(self.y))
        return round(math.degrees(math.acos(
            self.__mul__(other) / (self.get_length() * other.get_length()),
        )))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_point=(self.x * math.cos(math.radians(degrees))
                     - self.y * math.sin(math.radians(degrees))),

            y_point=(self.x * math.sin(math.radians(degrees))
                     + self.y * math.cos(math.radians(degrees))),
        )
