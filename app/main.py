import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x, self.coord_y = round(coord_x, 2), round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.coord_x + other.coord_x, self.coord_y + other.coord_y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.coord_x - other.coord_x, self.coord_y - other.coord_y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.coord_x * other, self.coord_y * other)
        return round(self.coord_x * other.coord_x + self.coord_y * other.coord_y, 4)

    @classmethod
    def create_vector_by_two_points(
        cls, start: tuple[float, float], end: tuple[float, float]
    ) -> "Vector":
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.coord_x**2 + self.coord_y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(self.coord_x / length, self.coord_y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_angle = max(
            -1.0,
            min(1.0, (self * other) / (self.get_length() * other.get_length())),
        )
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle, sin_angle = math.cos(radians), math.sin(radians)
        return Vector(
            self.coord_x * cos_angle - self.coord_y * sin_angle,
            self.coord_x * sin_angle + self.coord_y * cos_angle,
        )