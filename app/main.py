import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other: float) -> "Vector":
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0

        dot_product = self * other
        cos_value = dot_product / length_product
        cos_value = max(-1.0, min(1.0, cos_value))

        angle = math.degrees(math.acos(cos_value))
        return round(angle)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0

        cos_value = self.y / length
        cos_value = max(-1.0, min(1.0, cos_value))

        angle = math.degrees(math.acos(cos_value))
        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_value = math.cos(radians)
        sin_value = math.sin(radians)

        new_x = self.x * cos_value - self.y * sin_value
        new_y = self.x * sin_value + self.y * cos_value

        return Vector(new_x, new_y)
