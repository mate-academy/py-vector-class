import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord + other.x_coord, self.y_coord + other.y_coord
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord - other.x_coord, self.y_coord - other.y_coord
        )

    def __mul__(
            self, other: Union["Vector", float, int]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        elif isinstance(other, (int, float)):
            return Vector(self.x_coord * other, self.y_coord * other)
        else:
            raise TypeError("Невідома операція")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_angle = dot_product / (length_self * length_other)
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.y_coord, self.x_coord))
        return angle if angle >= 0 else angle + 360

    def rotate(self, degrees: float) -> "Vector":
        rad = math.radians(degrees)
        x_new = self.x_coord * math.cos(rad) - self.y_coord * math.sin(rad)
        y_new = self.x_coord * math.sin(rad) + self.y_coord * math.cos(rad)
        return Vector(x_new, y_new)
