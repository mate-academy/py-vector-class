import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operand must be an instance of Vector")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Operand must be an instance of Vector")

    def __mul__(
        self, scalar: Union[int, float, "Vector"]
    ) -> Union["Vector", float]:
        if isinstance(scalar, Vector):
            return self.x * scalar.x + self.y * scalar.y
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        else:
            raise TypeError("Operand must be a number")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        if len(start_point) != 2 or len(end_point) != 2:
            raise ValueError(
                "Both start_point and end_point must be tuples of length 2"
            )
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = math.hypot(self.x, self.y)
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        if not isinstance(other, Vector):
            raise TypeError("Operand must be an instance of Vector")
        dot_product = self.x * other.x + self.y * other.y
        length_self = math.hypot(self.x, self.y)
        length_other = math.hypot(other.x, other.y)
        if length_self == 0 or length_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = max(
            -1.0, min(1.0, dot_product / (length_self * length_other))
        )
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, angle: float) -> "Vector":
        radians = math.radians(angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
