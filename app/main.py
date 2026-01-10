from typing import Union
from math import sqrt, acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, coordinate_x: float | int,
                 coordinate_y: float | int) -> None:
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

    def __mul__(self, other: Union["Vector", int, float]) -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )

        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: "Vector") -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        len1, len2 = self.get_length(), other.get_length()

        cos_angle = dot_product / (len1 * len2)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        return round(degrees(acos(cos_angle)))

    def get_angle(self) -> int | float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        return Vector(self.x * cos(radians(degrees))
                      - self.y * sin(radians(degrees)),
                      self.x * sin(radians(degrees))
                      + self.y * cos(radians(degrees)))
