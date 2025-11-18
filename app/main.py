from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cor: int | float, y_cor: int | float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float],
                                    end_point: tuple[float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_a = self.get_length()
        len_b = other.get_length()

        if len_a == 0 or len_b == 0:
            return 0

        cos_a = dot / (len_a * len_b)
        cos_a = max(-1.0, min(1.0, cos_a))
        angle = math.degrees(math.acos(cos_a))
        return int(round(angle))

    def get_angle(self) -> float:
        return int(round(math.degrees(math.acos(self.y / self.get_length()))))

    def rotate(self, angle: float) -> Vector:
        rad = math.radians(angle)
        return Vector(self.x * math.cos(rad) - self.y * math.sin(rad),
                      self.x * math.sin(rad) + self.y * math.cos(rad))
