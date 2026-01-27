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
        other: Union["Vector", float, int],
    ) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

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
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        lengths_product = self.get_length() * vector.get_length()
        cos_angle = dot_product / lengths_product
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )
        rotated_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )
        return Vector(rotated_x, rotated_y)
