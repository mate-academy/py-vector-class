from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: int | float, y_cord: int | float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return float(self.x * other.x + self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def __rmul__(self, other: Vector) -> Vector:
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector | None:
        length = self.get_length()
        if length == 0:
            return None
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int | None:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return None
        cos_angle = dot_product / length_product
        cos_angle = min(1, max(cos_angle, -1))
        angle_radians = math.acos(cos_angle)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> float:
        result = round(math.degrees(math.atan2(self.x, self.y)))
        if result < 0:
            result -= (result * 2)
        return result

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
