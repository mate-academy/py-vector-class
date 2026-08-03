from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self._x = float(f"{x_coord: .2f}")
        self._y = float(f"{y_coord: .2f}")

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other,
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Angle with zero-length vector is undefined")
        cos_angle = dot / (len_self * len_other)
        cos_angle = max(min(cos_angle, 1), -1)
        angle = math.degrees(math.acos(cos_angle))
        return int(round(angle))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError("Angle for zero vector is undefined")
        cos_angle = self.y / length
        cos_angle = max(min(cos_angle, 1), -1)
        angle = math.degrees(math.acos(cos_angle))
        return int(round(angle))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
