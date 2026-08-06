from __future__ import annotations
import math as m


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector | int | float) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        product = (self * other) / (self.get_length() * other.get_length())

        degrees = m.degrees(m.acos(product))

        return round(degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle_d: float) -> Vector:
        angle_r = m.radians(angle_d)

        x2 = m.cos(angle_r) * self.x - m.sin(angle_r) * self.y

        y2 = m.sin(angle_r) * self.x + m.cos(angle_r) * self.y

        return Vector(x2, y2)
