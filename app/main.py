from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, s_point: tuple, e_point: tuple
    ) -> Vector:
        coord_x = e_point[0] - s_point[0]
        coord_y = e_point[1] - s_point[1]
        return cls(coord_x, coord_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_prod = self * other
        length1 = self.get_length()
        length2 = other.get_length()
        if length1 == 0 or length2 == 0:
            raise ValueError(
                "Cannot calculate the angle with zero-length vector"
            )
        cos_angle = dot_prod / (length1 * length2)
        cos_angle = max(min(cos_angle, 1), -1)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.x, self.y))
        return round(abs(angle))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
