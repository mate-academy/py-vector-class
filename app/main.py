import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    @property
    def x(self) -> float:
        return self.x_coord

    @property
    def y(self) -> float:
        return self.y_coord

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord + other.x_coord,
            self.y_coord + other.y_coord
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord
        )

    def __mul__(
        self, other: Union["Vector", float, int]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return (
                self.x_coord * other.x_coord + self.y_coord * other.y_coord
            )
        if isinstance(other, (int, float)):
            return Vector(
                self.x_coord * other,
                self.y_coord * other
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.hypot(self.x_coord, self.y_coord)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(
            round(self.x_coord / length, 2),
            round(self.y_coord / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot = (
            self.x_coord * other.x_coord + self.y_coord * other.y_coord
        )
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cos_angle = dot / (len_self * len_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_angle = self.y_coord / length
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = (
            self.x_coord * math.cos(radians) - self.y_coord * math.sin(radians)
        )
        rotated_y = (
            self.x_coord * math.sin(radians) + self.y_coord * math.cos(radians)
        )
        return Vector(round(rotated_x, 2), round(rotated_y, 2))
