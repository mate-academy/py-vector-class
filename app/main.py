from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def angle_between(self, other: Vector) -> int:
        cos_ = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degree: int) -> Vector:
        # degree_axis_x = self.angle_between(Vector(abs(self.x), 0))
        # degree_axis_x = self.get_angle()
        radiant_angle = math.radians(degree)
        x_point = (self.x * math.cos(radiant_angle)
                   - self.y * math.sin(radiant_angle))
        y_point = (self.x * math.sin(radiant_angle)
                   + self.y * math.cos(radiant_angle))
        return Vector(x_point, y_point)
