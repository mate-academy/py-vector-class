from __future__ import annotations
import math


class Vector:
    def __init__(self, letter_x: float | int, letter_y: float | int) -> None:

        if isinstance(letter_x, int):
            self.x = letter_x
        self.x = round(letter_x, 2)
        if isinstance(letter_y, int):
            self.y = letter_y
        self.y = round(letter_y, 2)

    def __add__(self, other: Vector) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> object:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> int | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2),
                      round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        start = Vector(start_point[0], start_point[1])
        end = Vector(end_point[0], end_point[1])
        result = end - start
        return cls(result.x, result.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> object:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, vector: Vector) -> int:
        scalar_vectors = self.__mul__(vector)
        modules_vector_x = self.get_length()
        modules_vector_y = vector.get_length()
        cos_a = scalar_vectors / (modules_vector_x * modules_vector_y)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, degrees: int) -> object:
        angle_radians = math.radians(degrees)
        return Vector(math.cos(angle_radians) * self.x
                      + - math.sin(angle_radians) * self.y,
                      math.sin(angle_radians) * self.x
                      + math.cos(angle_radians) * self.y)
