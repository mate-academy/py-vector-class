import math
from typing import Union


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.end_x = round(end_x, 2)
        self.end_y = round(end_y, 2)

    @property
    def x(self) -> float:
        return self.end_x

    @property
    def y(self) -> float:
        return self.end_y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.end_x + other.end_x, self.end_y + other.end_y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.end_x - other.end_x, self.end_y - other.end_y)

    def __mul__(
            self,
            other: Union[int, float, "Vector"]
    ) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.end_x * other, self.end_y * other)
        elif isinstance(other, Vector):
            return self.end_x * other.end_x + self.end_y * other.end_y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        delta_x = end_x - start_x
        delta_y = end_y - start_y
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.end_x ** 2 + self.end_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.end_x / length, self.end_y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        angle_radians = math.acos(
            dot_product / (self.get_length() * other.get_length())
        )
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.end_y, self.end_x)
        angle_degrees = math.degrees(angle_radians)
        positive_angle = (90 - angle_degrees) % 360
        clockwise_angle = (360 - positive_angle) % 360
        return round(clockwise_angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.end_x * math.cos(radians) - self.end_y * math.sin(radians)
        new_y = self.end_x * math.sin(radians) + self.end_y * math.cos(radians)
        return Vector(new_x, new_y)
