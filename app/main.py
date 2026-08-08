from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(coord_x=self.x + other.x, coord_y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(coord_x=self.x - other.x, coord_y=self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(coord_x=round(self.x * other, 2), coord_y=round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            coord_x=end_point[0] - start_point[0],
            coord_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            coord_x=round(self.x / self.get_length(), 2),
            coord_y=round(self.y / self.get_length(), 2)
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
        return Vector(coord_x=new_x, coord_y=new_y)
