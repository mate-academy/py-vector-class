from typing import Any
import math


class Vector:

    def __init__(self, x: float | int, y: float | int) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 4)
        return NotImplemented

    def __rmul__(self, other: Any) -> Any:
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        lenght = self.get_length()
        if lenght == 0:
            return Vector(0, 0)
        return Vector(self.x / lenght, self.y / lenght)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            return 0

        cos_a = dot_product / (len_self * len_other)
        cos_a = max(-1.0, min(1.0, cos_a))

        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> int:
        unit_y = Vector(0, 1)
        return self.angle_between(unit_y)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_r = math.cos(rad)
        sin_r = math.sin(rad)

        new_x = self.x * cos_r - self.y * sin_r
        new_y = self.x * sin_r + self.y * cos_r

        return Vector(new_x, new_y)
