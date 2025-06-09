import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union["Vector", float, int]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            dot = self.x * other.x + self.y * other.y
            return round(dot, 4)
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        return cls(dx, dy)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
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
        cos_angle = self.y / length
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = (
            self.x * math.cos(radians) - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
        return Vector(round(new_x, 2), round(new_y, 2))
