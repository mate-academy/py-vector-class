from __future__ import annotations
import math


class Vector:

    def __init__(self, coordinates_x: float | int,
                 coordinates_y: float | int) -> None:
        self.x = round(coordinates_x, 2)
        self.y = round(coordinates_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, other: Vector | int) -> float:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        else:
            mul_x = round(self.x * other, 2)
            mul_y = round(self.y * other, 2)
            return Vector(mul_x, mul_y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        created_x = end_point[0] - start_point[0]
        created_y = end_point[1] - start_point[1]
        return cls(created_x, created_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector2: tuple) -> int:
        if isinstance(vector2, Vector):
            cos_a = Vector.__mul__(self, vector2) \
                / (Vector.get_length(self) * Vector.get_length(vector2))
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / Vector.get_length(self))))

    def rotate(self, degrees: int) -> Vector:
        rotated_x = math.cos(math.radians(degrees)) * self.x - \
            math.sin(math.radians(degrees)) * self.y
        rotated_y = math.sin(math.radians(degrees)) * self.x + \
            math.cos(math.radians(degrees)) * self.y
        return Vector(rotated_x, rotated_y)
