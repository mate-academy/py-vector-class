from typing import Union
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:

    def __init__(self, x_c: Union[int, float], y_c: Union[int, float]) -> None:
        self.x = round(float(x_c), 2)
        self.y = round(float(y_c), 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(x_c=self.x + other.x, y_c=self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(x_c=self.x - other.x, y_c=self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float]) -> (
            Union)["Vector", int, float]:
        if isinstance(other, (int, float)):
            return Vector(x_c=self.x * other, y_c=self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            raise TypeError("Operand must be a Vector instance or a number.")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        if len(start_point) < 2 or len(end_point) < 2:
            raise ValueError(
                "Both elements must have at least two elements."
            )
        x_cord = end_point[0] - start_point[0]
        y_cord = end_point[1] - start_point[1]
        return cls(x_cord, y_cord)

    def get_length(self) -> Union[int, float]:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            x_c=round(self.x / length, 2),
            y_c=round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        scalar_mult = (self.x * other.x) + (self.y * other.y)
        self_length = self.get_length()
        other_length = other.get_length()
        cos_a = scalar_mult / (self_length * other_length)
        result = degrees(acos(cos_a))
        return int(result) + (result > int(result))

    def get_angle(self) -> int:
        self_length = self.get_length()
        cos_a = self.y / self_length
        return int(degrees(acos(cos_a)))

    def rotate(self, degree: int) -> "Vector":
        rad_degree = radians(degree)
        a_cord = (self.x * cos(rad_degree)) - (self.y * sin(rad_degree))
        b_cord = (self.x * sin(rad_degree)) + (self.y * cos(rad_degree))
        return Vector(x_c=round(a_cord, 2), y_c=round(b_cord, 2))
