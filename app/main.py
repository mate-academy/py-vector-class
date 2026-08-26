import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 3)
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple,
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2),
        )

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        len_product = self.get_length() * other.get_length()
        if len_product == 0:
            return 0
        cos_a = max(min(dot / len_product, 1), -1)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_a = self.y / length
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = (
            self.x * math.cos(radians) - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
        return Vector(new_x, new_y)
