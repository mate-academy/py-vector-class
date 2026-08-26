from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        x_coord = self.x + other.x
        y_coord = self.y + other.y
        return Vector(x_coord, y_coord)

    def __sub__(self, other: Vector) -> Vector:
        x_coord = self.x - other.x
        y_coord = self.y - other.y
        return Vector(x_coord, y_coord)

    def __mul__(self, other: int | Vector) -> Vector | float:
        if not isinstance(other, Vector):
            x_coord = self.x * other
            y_coord = self.y * other
            return Vector(x_coord, y_coord)
        else:
            x_coord = self.x * other.x
            y_coord = self.y * other.y
            return x_coord + y_coord

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        length = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        return length

    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        magnitude = self.magnitude()
        x_coord = self.x / magnitude
        y_coord = self.y / magnitude
        return Vector(x_coord, y_coord)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        mag_self = self.magnitude()
        mag_other = other.magnitude()
        cos_a = dot / (mag_self * mag_other)

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        dot = self.y
        mag_self = self.magnitude()
        cos_a = dot / mag_self

        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_rot = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_rot = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_rot, y_rot)
