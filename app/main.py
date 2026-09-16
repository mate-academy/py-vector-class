from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def __add__(self: Vector, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self: Vector, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self: Vector, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def get_length(self: Vector) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self: Vector) -> float:
        return Vector(
            self.x / round(self.get_length(), 1),
            self.y / round(self.get_length(), 1),
        )

    def angle_between(self: Vector, other: Vector) -> int:
        scalar = self.x * other.x + self.y * other.y
        angle = math.degrees(
            math.acos(scalar / (self.get_length() * other.get_length()))
        )
        return math.ceil(angle)

    def get_angle(self: Vector) -> int:
        scalar = self.x * 0 + self.y * 1
        length = self.get_length()

        res = math.acos(scalar / length)
        return int(math.degrees(res))

    def rotate(self: Vector, angle: int) -> Vector:
        angle = math.radians(angle)
        new_x = self.x * math.cos(angle) - self.y * math.sin(angle)
        new_y = self.x * math.sin(angle) + self.y * math.cos(angle)

        return Vector(new_x, new_y)
