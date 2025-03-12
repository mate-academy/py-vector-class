import math
from typing import Any


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)  # noqa: VNE001
        self.y = round(y, 2)  # noqa: VNE001

    def __add__(self, other: "Vector") -> Any:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
            ## 5 tests pass

    def __sub__(self, other: "Vector") -> Any:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
            ## 8 tests pass

    def __mul__(self, other: "Vector") -> Any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
            # after change 14 tests pass
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
            # 11 tests pass
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]  # noqa: VNE001
        y = end_point[1] - start_point[1]  # noqa: VNE001
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)  # 20 tests pass

    def get_normalized(self) -> Any:

        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        x = self.x / length  # noqa: VNE001
        y = self.y / length  # noqa: VNE001
        return Vector(round(x, 2), round(y, 2))
        # 23 tests pass

    def angle_between(self, other: "Vector") -> float:
        cos_theta = (self * other) / (self.get_length() * other.get_length())
        cos_theta = max(-1, min(1, cos_theta))
        return round(math.degrees(math.acos(cos_theta)), 0)
        # 26 tests pass

    def get_angle(self) -> int:
        cos_theta = self.y / self.get_length()
        cos_theta = max(-1, min(1, cos_theta))
        return int(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
