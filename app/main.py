from typing import Union
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: int | Vector | float
    ) -> Union["Vector", float, None]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return None

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        length = math.sqrt(self.x**2 + self.y**2)
        return length

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_multiply = self.x * other.x + self.y * other.y
        length_s = self.get_length()
        length_o = other.get_length()
        cos_alpha = max(-1.0, min(1.0, dot_multiply / (length_s * length_o)))
        angle_rad = math.acos(cos_alpha)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        length_s = self.get_length()
        dot_multiply = self.y / length_s
        cos_alpha = max(-1.0, min(1.0, dot_multiply))
        angle_deg = math.degrees(math.acos(cos_alpha))
        if self.x > 0:
            angle_deg = 360 - angle_deg
        return round(angle_deg)

    def rotate(self, degrees: float) -> "Vector":
        rad = math.radians(degrees)
        return Vector(
            x_coord=round(self.x * math.cos(rad) - self.y * math.sin(rad), 2),
            y_coord=round(self.x * math.sin(rad) + self.y * math.cos(rad), 2)
        )
