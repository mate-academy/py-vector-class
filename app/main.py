import math
from typing import Any


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def check_other(self, other: Any) -> Any:
        if not isinstance(other, Vector):
            return NotImplemented
        return False

    def __add__(self, other: "Vector") -> "Vector":
        if not self.check_other(other):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if not self.check_other(other):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple,
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        if self.check_other(other) is NotImplemented:
            return NotImplemented

        dot_product = self * other
        cos_angle = dot_product / (
            self.get_length() * other.get_length()
        )

        cos_angle = max(-1, min(1, cos_angle))

        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        cos_angle = max(-1, min(1, cos_angle))
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(new_x, new_y)
