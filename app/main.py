from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector_plus: Vector) -> Vector:
        return Vector(self.x + vector_plus.x, self.y + vector_plus.y)

    def __sub__(self, vector_plus: Vector) -> Vector:
        return Vector(self.x - vector_plus.x, self.y - vector_plus.y)

    def __mul__(self, vector_plus: float | Vector) -> float | Vector:
        if isinstance(vector_plus, Vector):
            return self.x * vector_plus.x + self.y * vector_plus.y
        else:
            return Vector(self.x * vector_plus, self.y * vector_plus)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vect) -> int:
        return round(math.degrees(math.acos(
            (self.x * vect.x + self.y * vect.y)
            / (self.get_length() * vect.get_length())
        )))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
