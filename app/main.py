from __future__ import annotations

import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

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

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if not isinstance(other, float | int):
            return self.x * other.x + self.y * other.y

        else:
            return Vector(
                self.x * other,
                self.y * other
            )

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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        mul_vectors = self.__mul__(other)
        len_vector_a = self.get_length()
        len_vector_b = other.get_length()
        cos_angle = mul_vectors / (len_vector_a * len_vector_b)

        return round(math.degrees((math.acos(cos_angle))))

    def get_angle(self) -> int:
        angle_x = math.degrees(math.atan2(self.y, self.x))
        if 0 <= angle_x < 90:
            angle_y = 90 - angle_x
        elif -90 <= angle_x < 0:
            angle_y = 90 + abs(angle_x)
        elif -180 <= angle_x < -90:
            angle_y = 270 + angle_x
        else:
            angle_y = angle_x - 90
        return round(angle_y)

    def rotate(self, degrees: float) -> Vector:
        rad = math.radians(degrees)

        coord_x = (self.x * math.cos(rad)
                   - self.y * math.sin(rad))
        coord_y = (self.x * math.sin(rad)
                   + self.y * math.cos(rad))

        return Vector(coord_x, coord_y)
