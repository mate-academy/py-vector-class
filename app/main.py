from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier: float | Vector) -> Vector | float:
        if isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y
        else:
            return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        answer_x = self.x / self.get_length()
        answer_x = round(answer_x, 2)
        answer_y = self.y / self.get_length()
        answer_y = round(answer_y, 2)
        return Vector(answer_x, answer_y)

    def angle_between(self, other: Vector) -> int:
        cos_a = ((self * other)
                 / (self.get_length() * other.get_length()))
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: float) -> Vector:
        x_new = (math.cos(math.radians(angle)) * self.x
                 - math.sin(math.radians(angle)) * self.y)
        y_new = (math.sin(math.radians(angle)) * self.x
                 + math.cos(math.radians(angle)) * self.y)
        return Vector(x_new, y_new)
