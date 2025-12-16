import math
from typing import Tuple, Union


Point = Tuple[float, float]


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: Union["Vector", int, float],
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Point,
        end_point: Point,
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        length_product = self.get_length() * vector.get_length()
        if length_product == 0:
            return 0
        cos_value = (self * vector) / length_product
        cos_value = max(-1.0, min(1.0, cos_value))
        return round(math.degrees(math.acos(cos_value)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_value = max(-1.0, min(1.0, self.y / length))
        return round(math.degrees(math.acos(cos_value)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_value = math.cos(radians)
        sin_value = math.sin(radians)
        return Vector(
            self.x * cos_value - self.y * sin_value,
            self.x * sin_value + self.y * cos_value,
        )
