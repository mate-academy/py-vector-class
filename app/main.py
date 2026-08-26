from __future__ import annotations
import math


class Vector:
    def __init__(self, x_arrow: float = 0.00, y_arrow: float = 0.00) -> None:
        self.x = round(x_arrow, 2)
        self.y = round(y_arrow, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" | float | int) -> "Vector" | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        cos_a = dot_product / (len_self * len_other)
        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        if self.y == 0 or self.x == 0:
            return 0
        angle_x_rad = math.atan2(self.y, self.x)
        angle_x_deg = math.degrees(angle_x_rad)
        angle_y_deg = 90 - angle_x_deg
        if angle_y_deg < 0:
            final_angle = abs(angle_y_deg)
        else:
            final_angle = abs(angle_y_deg - 360)
        return round(final_angle)

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        x_rotated = self.x * cos_a - self.y * sin_a
        y_rotated = self.x * sin_a + self.y * cos_a
        return Vector(round(x_rotated, 2), round(y_rotated, 2))
