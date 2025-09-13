import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        # store rounded to 2 decimals
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord + other.x_coord,
            self.y_coord + other.y_coord,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord,
        )

    def __mul__(
        self,
        other: Union["Vector", float, int],
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x_coord * other,
                self.y_coord * other,
            )
        if isinstance(other, Vector):
            # dot product
            return round(
                self.x_coord * other.x_coord
                + self.y_coord * other.y_coord,
                4,
            )
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_coord**2 + self.y_coord**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            self.x_coord / length,
            self.y_coord / length,
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = (
            self.x_coord * other.x_coord
            + self.y_coord * other.y_coord
        )
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_a = dot_product / length_product
        cos_a = max(-1, min(1, cos_a))  # clamp
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_a = self.y_coord / length
        cos_a = max(-1, min(1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x_coord = (
            self.x_coord * math.cos(radians)
            - self.y_coord * math.sin(radians)
        )
        new_y_coord = (
            self.x_coord * math.sin(radians)
            + self.y_coord * math.cos(radians)
        )
        return Vector(new_x_coord, new_y_coord)

    def __repr__(self) -> str:
        return (
            f"Vector(x_coord={self.x_coord}, "
            f"y_coord={self.y_coord})"
        )
