import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        coord_x_sum = self.coord_x + other.coord_x
        coord_y_sum = self.coord_y + other.coord_y
        return Vector(coord_x_sum, coord_y_sum)

    def __sub__(self, other: "Vector") -> "Vector":
        coord_x_diff = self.coord_x - other.coord_x
        coord_y_diff = self.coord_y - other.coord_y
        return Vector(coord_x_diff, coord_y_diff)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.coord_x * other, self.coord_y * other)

        dot_product = (
                self.coord_x * other.coord_x +
                self.coord_y * other.coord_y
        )
        return round(dot_product, 4)

    @classmethod
    def create_vector_by_two_points(
            cls, start: tuple[float, float], end: tuple[float, float]
    ) -> "Vector":
        coord_x_diff = end[0] - start[0]
        coord_y_diff = end[1] - start[1]
        return cls(coord_x_diff, coord_y_diff)

    def get_length(self) -> float:
        coord_x_squared = self.coord_x ** 2
        coord_y_squared = self.coord_y ** 2
        length = math.sqrt(coord_x_squared + coord_y_squared)
        return length

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")

        coord_x_normalized = self.coord_x / length
        coord_y_normalized = self.coord_y / length
        return Vector(coord_x_normalized, coord_y_normalized)

    def angle_between(self, other: "Vector") -> int:
        cos_angle = max(
            -1.0,
            min(
                1.0,
                (self * other) / (self.get_length() * other.get_length())
            ),
        )
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)

        coord_x_rotated = (
                self.coord_x * cos_angle -
                self.coord_y * sin_angle
        )
        coord_y_rotated = (
                self.coord_x * sin_angle +
                self.coord_y * cos_angle
        )

        return Vector(coord_x_rotated, coord_y_rotated)
