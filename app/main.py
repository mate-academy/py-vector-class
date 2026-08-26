import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    __rmul__ = __mul__

    def __truediv__(self, divisor: float) -> "Vector":
        return Vector(self.x / divisor, self.y / divisor)

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
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        dot = self * other
        cos_angle = dot / (len_self * len_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_to_y = self.y / length
        cos_to_y = max(-1.0, min(1.0, cos_to_y))
        return round(math.degrees(math.acos(cos_to_y)))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cos_val = math.cos(radians)
        sin_val = math.sin(radians)
        new_x = self.x * cos_val - self.y * sin_val
        new_y = self.x * sin_val + self.y * cos_val
        return Vector(new_x, new_y)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
