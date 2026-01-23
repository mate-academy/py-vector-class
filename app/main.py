from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: int) -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int) -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> Vector | float:
        if isinstance(other, Vector):
            dot = self.x * other.x + self.y * other.y
            return float(dot)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector | int | float:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        lengths = self.get_length() * other.get_length()
        if lengths == 0:
            return 0
        cos_a = dot_product / lengths
        cos_a = max(min(cos_a, 1.0), -1.0)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        dot_product = self.y
        length = self.get_length()
        if length == 0:
            return 0
        cos_a = dot_product / length
        cos_a = max(min(cos_a, 1.0), -1.0)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
