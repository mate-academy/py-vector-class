import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()

        if length_product == 0:
            return 0

        cos_a = dot_product / length_product
        cos_a = max(-1.0, min(1.0, cos_a))

        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0

        cos_a = self.y / length
        cos_a = max(-1.0, min(1.0, cos_a))

        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        return Vector(new_x, new_y)