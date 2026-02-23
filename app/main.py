import math
from typing import Tuple, Self


class Vector:
    def __init__(self, pos_x: float, pos_y: float) -> None:
        self.pos_x = round(pos_x, 2)
        self.pos_y = round(pos_y, 2)

    def __add__(self, other: Self) -> Self:
        return Vector(self.pos_x + other.pos_x, self.pos_y + other.pos_y)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.pos_x - other.pos_x, self.pos_y - other.pos_y)

    def __mul__(self, other: Self) -> Self:
        return Vector(self.pos_x * other.pos_x, self.pos_y * other.pos_y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> Self:
        """Tworzy wektor na podstawie dwóch punktów."""
        diff_x = end_point[0] - start_point[0]
        diff_y = end_point[1] - start_point[1]
        return cls(diff_x, diff_y)

    def get_length(self) -> float:
        return math.sqrt(self.pos_x ** 2 + self.pos_y ** 2)

    def get_normalized(self) -> Self:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.pos_x / length, self.pos_y / length)

    def angle_between(self, other: Self) -> float:
        dot_product = self.pos_x * other.pos_x + self.pos_y * other.pos_y
        magnitudes = self.get_length() * other.get_length()
        if magnitudes == 0:
            return 0.0
        cos_theta = dot_product / magnitudes
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_rad = math.acos(cos_theta)
        return float(round(math.degrees(angle_rad)))
