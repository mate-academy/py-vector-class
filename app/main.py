from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_coord=self.x + other.x, y_coord=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_coord=self.x - other.x, y_coord=self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(x_coord=self.x * other, y_coord=self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        return Vector(
            x_coord=self.x / self.get_length(),
            y_coord=self.y / self.get_length()
        )

    def angle_between(self, vector: object) -> float:
        skal = (self.x * vector.x) + (self.y * vector.y)
        leng_self = self.get_length()
        leng_vector = vector.get_length()
        cos_u = skal / (leng_self * leng_vector)
        return round(math.degrees(math.acos(cos_u)))

    def get_angle(self) -> float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> object:
        rad = math.radians(degrees)
        cos_rad = math.cos(rad)
        sin_rad = math.sin(rad)
        new_x = self.x * cos_rad - self.y * sin_rad
        new_y = self.x * sin_rad + self.y * cos_rad
        return Vector(round(new_x, 2), round(new_y, 2))
