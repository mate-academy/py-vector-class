from __future__ import annotations
import math


class Vector:
    def __init__(self, xx: float, yy: float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, vect: Vector) -> Vector:
        return Vector(self.x + vect.x, self.y + vect.y)

    def __sub__(self, vect: Vector) -> Vector:
        return Vector(self.x - vect.x, self.y - vect.y)

    def __mul__(self, factor: int | float | Vector) -> int | float:
        if isinstance(factor, Vector):
            return self.x * factor.x + self.y * factor.y
        return Vector(self.x * factor, self.y * factor)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        ratio = self.get_length()
        return Vector(round(self.x / ratio, 2), round(self.y / ratio, 2))

    def angle_between(self, vect: Vector) -> float:
        dot = round(self.x * vect.x + self.y * vect.y, 2)
        mag1 = self.get_length()
        mag2 = vect.get_length()

        if mag1 == 0 or mag2 == 0:
            return None

        cos_theta = dot / (mag1 * mag2)
        cos_theta = max(-1, min(1, cos_theta))
        angle_degree = math.degrees(math.acos(cos_theta))
        return int(round(angle_degree, 0))

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.x, self.y))
        return abs(int(round(angle, 1)))

    def rotate(self, rotation: int) -> Vector:
        radians = math.radians(rotation)
        x2 = self.x * math.cos(radians) - self.y * math.sin(radians)
        y2 = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x2, y2)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])
