from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, other: Vector) -> int:
        magnitude_first = self.get_length()
        magnitude_second = other.get_length()
        dot_product = self.__mul__(other)
        return round(
            math.degrees(math.acos
                         (dot_product / (magnitude_first * magnitude_second)))
        )

    def get_angle(self) -> int:
        y_axis = Vector(x_coord=0, y_coord=1)
        magnitude_vector = self.get_length()
        magnitude_y_axis = y_axis.get_length()
        dot_product = self.__mul__(y_axis)
        return round(
            math.degrees(math.acos
                         (dot_product / (magnitude_vector * magnitude_y_axis)))
        )

    def rotate(self, degrees: int) -> Vector:
        self.x, self.y = round(
            (math.cos(math.radians(degrees)) * self.x)
            - (math.sin(math.radians(degrees)) * self.y),
            2,
        ), round(
            (math.sin(math.radians(degrees)) * self.x)
            + (math.cos(math.radians(degrees)) * self.y),
            2,
        )
        return self


vector = Vector(33, 8)
vector2 = vector.rotate(45)

print(vector2.x)  # == 17.68
print(vector2.y)  # == 28.99
