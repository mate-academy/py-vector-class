from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            first: tuple,
            second: tuple
    ) -> Vector:
        return cls(second[0] - first[0], second[1] - first[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other: Vector) -> float:
        mul_ = (other.x * self.x) + (other.y * self.y)
        vector1 = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        vector2 = math.sqrt(pow(other.x, 2) + pow(other.y, 2))
        return math.ceil(math.degrees(math.acos(mul_ / (vector1 * vector2))))

    def get_angle(self) -> float:
        sum_ = (0 * self.x) + (10 * self.y)
        vector1 = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        vector2 = math.sqrt(pow(0, 2) + pow(10, 2))
        return math.floor(math.degrees(math.acos(sum_ / (vector1 * vector2))))

    def rotate(self, angel: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(angel))
            - self.y * math.sin(math.radians(angel)),
            self.y * math.cos(math.radians(angel))
            + self.x * math.sin(math.radians(angel))
        )
