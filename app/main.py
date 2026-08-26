from __future__ import annotations

import math


class Vector:
    def __init__(self, x_point: float, y_poiot: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_poiot, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | (int, float)) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector2: Vector) -> int:
        degrees = ((self.x * vector2.x + self.y * vector2.y)
                   / (math.sqrt(self.x ** 2 + self.y ** 2)
                      * math.sqrt(vector2.x ** 2 + vector2.y ** 2)))
        return round(math.degrees(math.acos(degrees)))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = abs(math.degrees(angle_rad))
        return round(angle_deg)

    def rotate(self, angle: int) -> Vector:
        angle_radians = math.radians(angle)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
