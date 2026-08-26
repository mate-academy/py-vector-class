import math
from typing import Union


class Vector:
    def __init__(self, initial_x: float, initial_y: float) -> None:
        self.x = round(float(initial_x), 2)
        self.y = round(float(initial_y), 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: Union["Vector", int, float]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot = self.x * other.x + self.y * other.y
        m1 = self.get_length()
        m2 = other.get_length()
        if m1 == 0 or m2 == 0:
            return 0
        cos_a = dot / (m1 * m2)
        cos_a = max(-1, min(1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        angle = abs(math.degrees(math.atan2(self.x, self.y)))
        return round(angle)

    def rotate(self, degrees: float) -> "Vector":
        rad = math.radians(degrees)
        cos_val = math.cos(rad)
        sin_val = math.sin(rad)
        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val
        return Vector(new_x, new_y)
