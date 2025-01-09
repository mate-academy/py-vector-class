import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.coord_x + other.coord_x,
            self.coord_y + other.coord_y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.coord_x - other.coord_x,
            self.coord_y - other.coord_y
        )

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(
                self.coord_x * other,
                self.coord_y * other
            )
        return round(
            self.coord_x * other.coord_x + self.coord_y * other.coord_y,
            5
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return round(
            math.sqrt(self.coord_x**2 + self.coord_y**2),
            5
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(
            round(self.coord_x / length, 2),
            round(self.coord_y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        cos_angle = max(
            -1.0,
            min(
                1.0,
                (self * other) / (self.get_length() * other.get_length())
            ),
        )
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        rotated_coord_x = round(
            self.coord_x * cos_angle - self.coord_y * sin_angle,
            2
        )
        rotated_coord_y = round(
            self.coord_x * sin_angle + self.coord_y * cos_angle,
            2
        )
        return Vector(rotated_coord_x, rotated_coord_y)
