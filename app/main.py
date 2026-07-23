import math
from typing import Union


class Vector:
    def __init__(
        self,
        coordinate_x: float,
        coordinate_y: float
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(
        self,
        other: Union["Vector", float]
    ) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return (
                self.x * other.x
                + self.y * other.y
            )

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        coordinate_x = end_point[0] - start_point[0]
        coordinate_y = end_point[1] - start_point[1]

        return cls(
            coordinate_x,
            coordinate_y
        )

    def get_length(self) -> float:
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector

        cos_angle = dot_product / (
            self.get_length()
            * vector.get_length()
        )

        angle = math.degrees(
            math.acos(cos_angle)
        )

        return round(angle)

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)

        return self.angle_between(
            positive_y_axis
        )

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

        return Vector(
            round(rotated_x, 2),
            round(rotated_y, 2)
        )
