from __future__ import annotations
import math


class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = round(float(x), 2)
        self.y = round(float(y), 2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmul__(self, other: float | Vector) -> float | Vector:
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Неможливо нормалізувати нульовий вектор.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        """Кут між векторами (ціле число в градусах)."""
        a_len = self.get_length()
        b_len = other.get_length()
        if a_len == 0 or b_len == 0:
            raise ValueError("Кут з нульовим вектором не визначений.")
        cos_value = (self.x * other.x + self.y * other.y) / (a_len * b_len)
        cos_value = max(-1.0, min(1.0, cos_value))
        return int(round(math.degrees(math.acos(cos_value))))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError("Кут нульового вектора не визначений.")
        cos_value = self.y / length
        cos_value = max(-1.0, min(1.0, cos_value))
        return int(round(math.degrees(math.acos(cos_value))))

    def rotate(self, degrees_value: int) -> Vector:
        theta = math.radians(degrees_value)
        cos_value = math.cos(theta)
        sin_value = math.sin(theta)
        new_x = self.x * cos_value - self.y * sin_value
        new_y = self.x * sin_value + self.y * cos_value
        return Vector(new_x, new_y)
