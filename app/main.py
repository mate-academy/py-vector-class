from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None: # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        elif isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        elif isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        if len(start_point) != 2 or len(end_point) != 2:
            raise ValueError("Points must have exactly two coordinates")
        dx = round(end_point[0] - start_point[0], 2)
        dy = round(end_point[1] - start_point[1], 2)
        return cls(dx, dy)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot calculate angle with zero vector")
        cos_theta = dot_product / (len_self * len_other)
        # Обмежуємо значення, щоб уникнути похибок з плаваючою точкою
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_deg = math.degrees(math.acos(cos_theta))
        return int(round(angle_deg))

    def get_angle(self) -> int:
        angle = (360 - math.degrees(math.atan2(self.x, self.y))) % 360
        return int(round(angle))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)

        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a

        # Округлення до 2 знаків після коми, як в умові
        return Vector(round(new_x, 2), round(new_y, 2))
