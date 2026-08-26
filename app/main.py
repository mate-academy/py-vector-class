import math
from typing import Tuple, Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: Union["Vector", int, float],
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            return 0

        cos_value = dot_product / lengths_product
        cos_value = max(-1, min(1, cos_value))
        angle = math.degrees(math.acos(cos_value))
        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.y, self.x))
        if angle < 0:
            angle += 360
        return round(angle)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cosine = math.cos(radians)
        sine = math.sin(radians)

        rotated_x = self.x * cosine - self.y * sine
        rotated_y = self.x * sine + self.y * cosine

        return Vector(rotated_x, rotated_y)
