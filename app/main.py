import math
from typing import Union, Tuple


class Vector:
    def __init__(self, coordinate1: float, coordinate2: float) -> None:
        self.x = round(coordinate1, 2)
        self.y = round(coordinate2, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

    def __mul__(
            self, other: Union["Vector", float, int]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return (self.x * other.x
                    + self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(
            end_x - start_x,
            end_y - start_y
        )

    def get_length(self) -> float:
        return math.sqrt(
            self.x ** 2 + self.y ** 2
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            self.x / length,
            self.y / length
        )

    def get_angle(self) -> float:
        vertical_vector = Vector(0, 1)
        angle = self.angle_between(vertical_vector)
        return round(angle, 2)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = (self.x * cos_theta
                 - self.y * sin_theta)
        y_new = (self.x * sin_theta
                 + self.y * cos_theta)
        return Vector(round(x_new, 2), round(y_new, 2))

    def angle_between(self, other: "Vector") -> float:
        if not isinstance(other, Vector):
            return NotImplemented
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            return 0.0
        cos_angle = dot_product / (
            length_self * length_other
        )
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)
