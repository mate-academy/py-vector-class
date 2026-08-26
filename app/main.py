from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: object) -> NotImplemented | Vector:
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __sub__(self, other: object) -> NotImplemented | Vector:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)

    def __mul__(self, other: object) -> NotImplemented | float | Vector:
        if isinstance(other, Vector):
            dot = self.x * other.x + self.y * other.y
            return dot
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> None | Vector:
        if len(start_point) == 2 and len(end_point) == 2:
            start_x, start_y = start_point
            end_x, end_y = end_point
            dx = end_x - start_x
            dy = end_y - start_y
            return cls(dx, dy)

    def get_length(self) -> float:
        result = math.hypot(self.x, self.y)
        return result

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        nx = self.x / length
        ny = self.y / length
        return Vector(nx, ny)

    def angle_between(self, other: object) -> int:
        dot = self * other
        len1 = self.get_length()
        len2 = other.get_length()
        if len1 == 0 or len2 == 0:
            raise ValueError("zero-length vector")
        cos_a = dot / (len1 * len2)
        cos_a = min(1, max(-1, cos_a))
        angle_deg = math.degrees(math.acos(cos_a))
        return int(round(angle_deg))

    def get_angle(self) -> int:
        theta = math.degrees(math.atan2(self.y, self.x))
        angle = (theta - 90) % 360
        return int(round(angle))

    def rotate(self, degrees: int | float) -> Vector:
        theta = math.radians(degrees)
        cosinus = math.cos(theta)
        sinus = math.sin(theta)
        new_x = self.x * cosinus - self.y * sinus
        new_y = self.x * sinus + self.y * cosinus
        return Vector(new_x, new_y)
