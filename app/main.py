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

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            vec_x = self.x * other
            vec_y = self.y * other
            return Vector(vec_x, vec_y)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> Vector | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        magna = math.sqrt(self.x ** 2 + self.y ** 2)
        scalar = math.sqrt(other.x ** 2 + other.y ** 2)
        magna = magna * scalar
        cos_a = dot_product / magna
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        magnitude = math.sqrt(self.x ** 2 + self.y ** 2)
        arc = math.acos(self.y / magnitude)
        return round(math.degrees(arc))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_rotated = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_rotated = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_rotated, y_rotated)
