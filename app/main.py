from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        # sempre arredondar para 2 casas decimais
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            # produto escalar
            return self.x * other.x + self.y * other.y
        else:
            # multiplicação por escalar
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        dx = end_point[0] - start_point[0]
        dy = end_point[1] - start_point[1]
        return cls(dx, dy)

    def get_length(self) -> float:
        # comprimento sem arredondar
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        x_norm = self.x / length
        y_norm = self.y / length
        return Vector(x_norm, y_norm)

    def angle_between(self, other: Vector) -> int:
        # cos θ = (a·b)/(|a||b|)
        len1 = self.get_length()
        len2 = other.get_length()
        if len1 == 0 or len2 == 0:
            return 0
        cos_a = (self * other) / (len1 * len2)
        # limitar para [-1,1] para evitar math domain error
        cos_a = max(-1.0, min(1.0, cos_a))
        angle = math.degrees(math.acos(cos_a))
        return int(round(angle))

    def get_angle(self) -> int:
        # ângulo com o eixo Y positivo
        # cos θ = (v·(0,1))/|v| = y/|v|
        len_v = self.get_length()
        if len_v == 0:
            return 0
        cos_a = self.y / len_v
        cos_a = max(-1.0, min(1.0, cos_a))
        angle = math.degrees(math.acos(cos_a))
        return int(round(angle))

    def rotate(self, degrees: int) -> Vector:
        # rotação em graus anti-horária
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
