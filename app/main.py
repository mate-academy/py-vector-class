from __future__ import annotations
import math


class Vector:
    def __init__(self, x_var: float, y_var: float) -> None:
        self.x = round(x_var, 2)
        self.y = round(y_var, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_var=self.x + other.x,
            y_var=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_var=self.x - other.x,
            y_var=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            x_var=round(self.x * other, 2),
            y_var=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        return cls(
            x_var=end_point[0] - start_point[0],
            y_var=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_var=self.x / self.get_length(),
            y_var=self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        dot_product = (self.x * vector.x) + (self.y * vector.y)
        cos_func = dot_product / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_func)))

    def get_angle(self) -> int:
        cos_func = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_func)))

    def rotate(self, degrees: int) -> Vector:
        ang_rad = math.radians(degrees)

        x_new = self.x * math.cos(ang_rad) - self.y * math.sin(ang_rad)
        y_new = self.x * math.sin(ang_rad) + self.y * math.cos(ang_rad)

        return Vector(x_new, y_new)
