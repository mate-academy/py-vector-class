from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Vector | int) -> Vector | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(round(end_point[0] - start_point[0], 2),
                      round(end_point[1] - start_point[1], 2))

    def get_length(self: Vector) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self: Vector) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(math.acos(
            self * other / (round((self.x ** 2 + self.y ** 2) ** 0.5, 1)
                            * round((other.x ** 2 + other.y ** 2)
                                    ** 0.5, 1)))))

    def get_angle(self: Vector) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, other: int) -> Vector:
        radians = math.radians(other)
        x_value = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_value = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_value, 2), round(y_value, 2))
