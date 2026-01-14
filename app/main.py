from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> "Vector | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        dx = x2 - x1
        dy = y2 - y1
        return cls(dx, dy)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        elif length != 0:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int) -> int:
        dot = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cos_a = dot / (len_self * len_other)
        cos_a = max(-1, min(1, cos_a))
        rad = math.acos(cos_a)
        deg = math.degrees(rad)
        return int(round(deg))

    def get_angle(self) -> int:
        if self.get_length() == 0:
            return 0
        angle_x = math.degrees(math.atan2(self.y, self.x))
        angle = -(90 - angle_x) % 360
        angle = int(round(angle))
        return angle

    def rotate(self, degrees: Vector) -> "Vector":
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
