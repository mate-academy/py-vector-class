from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, multiplier: Vector | int | float) \
            -> Vector | int | float:
        if isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y

        return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()

        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, second_vector: Vector) -> int:
        angle_cos = (self * second_vector) / (self.get_length() * second_vector
                                              .get_length())

        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        result_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        result_y = math.sin(radians) * self.x + math.cos(radians) * self.y

        return Vector(result_x, result_y)
