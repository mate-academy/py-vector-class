from math import sqrt, acos, degrees, cos, sin, radians
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float])\
            -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return (
                Vector(self.x * other, self.y * other)
            )
        raise TypeError(
            "Multiplication is supported only with Vector or number"
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(round(normalized_x, 2), round(normalized_y, 2))

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ValueError(
                "Cannot calculate angle with a zero-length vector"
            )

        cos_a = dot_product / (length_self * length_other)
        angle = degrees(acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, angle_degrees: int) -> "Vector":
        radians_angle = radians(angle_degrees)
        rotated_x = (
            self.x * cos(radians_angle) - self.y * sin(radians_angle)
        )
        rotated_y = (
            self.x * sin(radians_angle) + self.y * cos(radians_angle)
        )
        return Vector(round(rotated_x, 2), round(rotated_y, 2))
