from __future__ import annotations
import math


class Vector:
    def __init__(self, x0: int | float, y0: int | float) -> None:
        self.x = round(x0, 2)
        self.y = round(y0, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)
        return NotImplemented

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        dx = x2 - x1
        dy = y2 - y1
        return cls(dx, dy)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            nx = self.x / length
            ny = self.y / length
            return Vector(nx, ny)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len1, len2 = self.get_length(), other.get_length()
        if abs(len1) < 1e-12 or abs(len2) < 1e-12:
            return 0
        cos_a = dot / (len1 * len2)
        cos_a = max(-1.0, min(1.0, cos_a))
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> int:
        if abs(self.x) < 1e-12 and abs(self.y) < 1e-12:
            return 0
        angle_x = math.degrees(math.atan2(self.y, self.x))
        angle_from_y = (90 - angle_x) % 360
        if angle_from_y > 180:
            angle_from_y = 360 - angle_from_y
        return round(angle_from_y)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        x1, y1 = self.x, self.y
        x_new = x1 * math.cos(rad) - y1 * math.sin(rad)
        y_new = x1 * math.sin(rad) + y1 * math.cos(rad)
        return Vector(x_new, y_new)
