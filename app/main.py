from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=round(self.x * other, 2), y=round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        cosinus = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosinus)))

    def get_angle(self) -> int:
        cosinus = self.y / self.get_length()
        return round(math.degrees(math.acos(cosinus)))

    def rotate(self, degrees: int) -> Vector:

        new_x = round(
            (self.x * math.cos(math.radians(degrees)))
            - (self.y * math.sin(math.radians(degrees))),
            2
        )
        new_y = round(
            (self.x * math.sin(math.radians(degrees)))
            + (self.y * math.cos(math.radians(degrees))),
            2
        )
        return Vector(x=new_x, y=new_y)
