from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[int, int], end_point: tuple[int, int]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    # used this func to make code simpler in the next one :)
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def angle_between(self, other: Vector) -> float:
        dot = self * other
        mag_prod = self.magnitude() * other.magnitude()
        angle_radian = math.acos(dot / mag_prod)

        angle_degrees = math.degrees(angle_radian)

        return round(angle_degrees)

    def get_angle(self) -> float:
        angle_rad = math.acos(self.y / self.magnitude())
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        x2 = self.x * math.cos(math.radians(degrees)) - self.y * math.sin(
            math.radians(degrees)
        )
        y2 = self.x * math.sin(math.radians(degrees)) + self.y * math.cos(
            math.radians(degrees)
        )
        return Vector(x2, y2)
