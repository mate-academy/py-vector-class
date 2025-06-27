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

    def __mul__(self, other: (int, float, Vector)) -> (int, float, Vector):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return abs(math.sqrt(self.x * self.x + self.y * self.y))

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        length = self.get_length() * other.get_length()
        cos_theta = max(min(dot / length, 1), -1)
        angle_rad = math.acos(cos_theta)

        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        length = self.get_length()

        cos_theta = self.y / length
        cos_theta = max(min(cos_theta, 1), -1)
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)
        x_new = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_new = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)

        return Vector(x_new, y_new)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple[int, float],
                                    end_point: tuple[int, float]) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )
