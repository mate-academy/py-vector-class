import math
from typing import Union

MultiplyType = Union["Vector", float]


class Vector:
    def __init__(self, horizontal: float, vertical: float) -> None:
        self.x = round(horizontal, 2)
        self.y = round(vertical, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> MultiplyType:
        if isinstance(other, float | int):
            return Vector(other * self.x, other * self.y)

        return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def angle_between(self, other: "Vector") -> int:
        self_length = self.get_length()
        other_length = other.get_length()

        magnitude = self * other

        cos = magnitude / (self_length * other_length)
        cos = max(-1.0, min(1.0, cos))

        angle_radians = math.acos(cos)
        angle_degrees = math.degrees(angle_radians)

        return int(round(angle_degrees, 0))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    first: tuple[float, float],
                                    second: tuple[float, float]
                                    ) -> "Vector":
        return cls(second[0] - first[0], second[1] - first[1])
