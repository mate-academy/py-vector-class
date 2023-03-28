from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x + other.x,
            point_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x - other.x,
            point_y=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector) is True:
            return self.x * other.x + self.y * other.y
        return Vector(point_x=self.x * other, point_y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            point_x=end_point[0] - start_point[0],
            point_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        point_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        point_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(point_x, point_y)
