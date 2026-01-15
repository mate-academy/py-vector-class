from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = round(self.x + other.x, 2)
        new_y = round(self.y + other.y, 2)
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = round(self.x - other.x, 2)
        new_y = round(self.y - other.y, 2)
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        x_coord = self.x / self.get_length()
        y_coord = self.y / self.get_length()
        return Vector(x_coord, y_coord)

    def angle_between(self, another_vector: Vector) -> int:
        cos_a = (self.__mul__(another_vector)
                 / (self.get_length() * another_vector.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_y = math.degrees(math.acos(self.y / self.get_length()))
        return round(cos_y)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_d = math.cos(radians)
        sin_d = math.sin(radians)
        rotated_x = self.x * cos_d - self.y * sin_d
        rotated_y = self.x * sin_d + self.y * cos_d

        return Vector(rotated_x, rotated_y)
