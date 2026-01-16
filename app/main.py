from __future__ import annotations
import math


class Vector:

    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other : Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other : Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (Vector, float, int)) -> float | Vector:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return (
            cls(end_point[0] - start_point[0], end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("error")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        fst = self.x * other.x + self.y * other.y
        snd = self.get_length() * other.get_length()
        third = math.degrees(math.acos(fst / snd))
        return round(third)

    def get_angle(self) -> int:
        fst = self.y
        snd = self.get_length()
        return round(math.degrees(math.acos(fst / snd)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
