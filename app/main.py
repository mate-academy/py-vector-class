from math import sqrt, acos, degrees, radians, cos, sin
from typing import Union, Tuple


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other_vector: "Vector") -> "Vector":
        return Vector(
            self.coord_x + other_vector.coord_x,
            self.coord_y + other_vector.coord_y,
        )

    def __sub__(self, other_vector: "Vector") -> "Vector":
        return Vector(
            self.coord_x - other_vector.coord_x,
            self.coord_y - other_vector.coord_y,
        )

    def __mul__(self, value: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(value, Vector):
            dot = (
                self.coord_x * value.coord_x
                + self.coord_y * value.coord_y
            )
            return round(dot, 4)
        return Vector(
            round(self.coord_x * value, 2),
            round(self.coord_y * value, 2),
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return sqrt(self.coord_x**2 + self.coord_y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        norm_x = round(self.coord_x / length, 2)
        norm_y = round(self.coord_y / length, 2)
        return Vector(norm_x, norm_y)

    def angle_between(self, other_vector: "Vector") -> int:
        dot = self * other_vector
        len_self = self.get_length()
        len_other = other_vector.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cosine = dot / (len_self * len_other)
        if cosine > 1:
            cosine = 1
        if cosine < -1:
            cosine = -1
        return round(degrees(acos(cosine)))

    def get_angle(self) -> int:
        axis_y = Vector(0.0, 1.0)
        return self.angle_between(axis_y)

    def rotate(self, degrees_value: int) -> "Vector":
        angle_rad = radians(degrees_value)
        rotated_x = (
            self.coord_x * cos(angle_rad)
            - self.coord_y * sin(angle_rad)
        )
        rotated_y = (
            self.coord_x * sin(angle_rad)
            + self.coord_y * cos(angle_rad)
        )
        return Vector(round(rotated_x, 2), round(rotated_y, 2))
