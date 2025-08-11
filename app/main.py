from math import sqrt, hypot, degrees, acos, sin, cos
from typing import Optional


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.coord_x + other.coord_x,
                      self.coord_y + other.coord_y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.coord_x - other.coord_x,
                      self.coord_y - other.coord_y)

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, Vector):
            return self.coord_x * other.coord_x + self.coord_y * other.coord_y
        return Vector(self.coord_x * other, self.coord_y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: "Vector",
                                    end_point: "Vector") -> "Vector":
        return Vector(end_point.coord_x - start_point.coord_x,
                      end_point.coord_y - start_point.coord_y)

    def get_length(self) -> float:
        return sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_normalized(self) -> Optional["Vector"]:
        if self.get_length() == 0:
            return None
        length = hypot(self.coord_x, self.coord_y)
        return Vector(self.coord_x / length, self.coord_y / length)

    def angle_between(self, other: "Vector") -> Optional[float]:
        dot_product = self.coord_x * other.coord_x + self.coord_y * other.coord_y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return None
        cos_angle = max(-1, min(1, dot_product / (len_other * len_self)))
        return round(degrees(acos(cos_angle)))

    def get_angle(self) -> Optional[float]:
        dot_product = self.coord_x * 0 + self.coord_y * 1
        len_self = self.get_length()
        len_other = 1
        if len_self == 0:
            return None
        cos_angle = max(-1, min(1, dot_product / (len_other * len_self)))
        return round(degrees(acos(cos_angle)))

    def rotate(self, angle_degrees: float) -> "Vector":
        rad = angle_degrees * (3.141592653589793 / 180)
        cos_b = cos(rad)
        sin_b = sin(rad)
        return Vector(
            self.coord_x * cos_b - self.coord_y * sin_b,
            self.coord_x * sin_b + self.coord_y * cos_b
        )
