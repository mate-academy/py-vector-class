from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, xez: float, yez: float) -> None:
        self.x = round(xez, 2)
        self.y = round(yez, 2)

    def __add__(self, other: Vector) -> Vector:
        result_x = self.x + other.x
        result_y = self.y + other.y
        return Vector(result_x, result_y)

    def __sub__(self, other: Vector) -> Vector:
        result_x = self.x - other.x
        result_y = self.y - other.y
        return Vector(result_x, result_y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(
                self.x * other,
                self.y * other
            )
        return self.x * other.x + self.y * other.y

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

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        angle_cos = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, angle: int) -> Vector:
        radian = math.radians(angle)
        return Vector(
            self.x * math.cos(radian) - self.y * math.sin(radian),
            self.y * math.cos(radian) + self.x * math.sin(radian)
        )
