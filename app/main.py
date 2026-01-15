import math
from typing import Tuple


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(round(delta_x, 2), round(delta_y, 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def _calculate_angle(self, other: "Vector") -> float:
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            return 0

        cos_angle = dot_product / (length_self * length_other)
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def angle_between(self, other: "Vector") -> float:
        return self._calculate_angle(other)

    def get_angle(self) -> float:
        y_vector = Vector(0, 1)
        return self._calculate_angle(y_vector)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = round(
            self.x * math.cos(radians) - self.y * math.sin(radians), 2
        )
        new_y = round(
            self.x * math.sin(radians) + self.y * math.cos(radians), 2
        )
        return Vector(new_x, new_y)
