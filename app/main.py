from typing import Union
from math import sqrt, acos, degrees, cos, sin, radians


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            (self.x + other.x),
            (self.y + other.y)
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            (self.x - other.x),
            (self.y - other.y)
        )

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float],
                                    end_point: tuple[float]) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(round(x_coord, 2), round(y_coord, 2))

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        return Vector(self.x, self.y)

    def get_angle(self) -> int:
        zero_vector = Vector(0, 1)
        return self.angle_between(zero_vector)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product != 0:
            radian = acos(dot_product / magnitude_product)
            return round(degrees(radian))
        return 0

    def rotate(self, degree: int) -> "Vector":
        cos_angle = cos(radians(degree))
        sin_angle = sin(radians(degree))
        x_coord = self.x * cos_angle - self.y * sin_angle
        y_coord = self.x * sin_angle + self.y * cos_angle
        return Vector(round(x_coord, 2), round(y_coord, 2))
