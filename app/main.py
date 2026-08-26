import math
from typing import Tuple, Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union[int, float, "Vector"]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                f"Unsupported operand type(s) for *: 'Vector' and "
                f"'{type(other).__name__}'"
            )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def get_angle(self) -> int:
        angle = (360 - math.degrees(math.atan2(self.x, self.y))) % 360
        return round(angle)

    def rotate(self, angle_degrees: float) -> "Vector":
        radians = math.radians(angle_degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(round(new_x, 2), round(new_y, 2))

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        len_product = self.get_length() * other.get_length()
        if len_product == 0:
            return 0
        cos_angle = max(min(dot / len_product, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    @classmethod
    def create_vector_by_two_points(
        cls, start: Tuple[float, float], end: Tuple[float, float]
    ) -> "Vector":
        return cls(end[0] - start[0], end[1] - start[1])
