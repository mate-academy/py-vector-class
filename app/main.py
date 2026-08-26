import math
from typing import Union


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                x_coordinate=self.x + other.x,
                y_coordinate=self.y + other.y,
            )

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                x_coordinate=self.x - other.x,
                y_coordinate=self.y - other.y,
            )

    def __mul__(self, other: Union["Vector", float, int]) -> (
            Union)["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, float | int):
            return Vector(
                x_coordinate=self.x * other,
                y_coordinate=self.y * other,
            )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:

        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        if self.get_length() != 0:
            return Vector(
                x_coordinate=self.x / self.get_length(),
                y_coordinate=self.y / self.get_length()
            )

    def angle_between(self, other: "Vector") -> int:
        if isinstance(other, Vector):
            cos_a = (self * other) / (self.get_length() * other.get_length())
        if -1 <= cos_a <= 1:
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:

        return self.angle_between(Vector(0, 1))

    def rotate(self, kyt: float) -> "Vector":
        rad = math.radians(kyt)

        return Vector(
            x_coordinate=self.x * math.cos(rad) - self.y * math.sin(rad),
            y_coordinate=self.x * math.sin(rad) + self.y * math.cos(rad)

        )
