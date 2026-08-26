import math
from typing import Union


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: Union["Vector", int, float]
    ) -> Union["Vector", float]:

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        mult = self * other
        mul_length = self.get_length() * other.get_length()

        if mul_length == 0:
            raise ValueError("Cannot compute angle with zero-length vector")

        cos_theta = mult / mul_length
        cos_theta = max(-1.0, min(1.0, cos_theta))  # clamp

        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        length = self.get_length()
        cos_theta = self.y / length
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, angle: float) -> "Vector":
        theta = math.radians(angle)
        new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        new_y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return Vector(new_x, new_y)
