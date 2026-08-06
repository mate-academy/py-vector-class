from __future__ import annotations
import math


class Vector:
    def __init__(
            self, coordinate_x: float | int, coordinate_y: int | float
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(other * self.x, other * self.y)
        if self.get_length() == 0 or other.get_length == 0:
            return 0
        cos = (self.x * other.x + self.y * other.y) / \
              (math.sqrt(self.x ** 2 + self.y ** 2)
               * math.sqrt(other.x ** 2 + other.y ** 2))
        return self.get_length() * other.get_length() * cos

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        toch1 = Vector(*start_point)
        toch2 = Vector(*end_point)
        return cls(toch2.x - toch1.x, toch2.y - toch1.y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        inv_lenght = 1 / self.get_length()
        return Vector(self.x * inv_lenght, self.y * inv_lenght)

    def angle_between(self, vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self.x * vector.x + self.y * vector.y)
                    / (math.sqrt(self.x ** 2 + self.y ** 2)
                       * math.sqrt(vector.x ** 2 + vector.y ** 2))
                )
            )
        )

    def get_angle(self) -> int | float:
        return round(
            math.degrees(
                math.acos(
                    (self.x * 0 + self.y * 1)
                    / math.sqrt(self.x ** 2 + self.y ** 2)
                    * math.sqrt(0 ** 2 + 1 ** 2)
                )
            )
        )

    def rotate(self, degrees: int) -> Vector:
        x2 = math.cos(math.radians(degrees)) * self.x \
            - math.sin(math.radians(degrees)) * self.y
        y2 = math.sin(math.radians(degrees)) * self.x \
            + math.cos(math.radians(degrees)) * self.y
        return Vector(x2, y2)
