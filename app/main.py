from __future__ import annotations
import math


class Vector:

    def __init__(self, x_co: float, y_co: float) -> None:
        self.x_co = round(x_co, 2)
        self.y_co = round(y_co, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x_co + other.x_co,
                self.y_co + other.y_co
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x_co - other.x_co,
                self.y_co - other.y_co
            )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x_co * other.x_co + self.y_co * other.y_co
        return Vector(self.x_co * other, self.y_co * other)

    @classmethod
    def create_vector_by_co_two_points(
            cls,
            start_point: tuple[int | float],
            end_point: tuple[int | float]) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_co ** 2 + self.y_co ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x_co / self.get_length(),
            self.y_co / self.get_length()
        )

    def angle_between(self, other: Vector) -> int | float:
        scalar_product = self.x_co * other.x_co + self.y_co * other.y_co
        self_length = self.get_length()
        other_length = other.get_length()
        cos_theta = scalar_product / (self_length * other_length)
        theta_radians = math.acos(cos_theta)
        return round(math.degrees(theta_radians))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        angle_radian = math.radians(angle)
        cos = math.cos(angle_radian)
        sin = math.sin(angle_radian)
        new_x_co = self.x_co * cos - self.y_co * sin
        new_y_co = self.x_co * sin + self.y_co * cos
        return Vector(new_x_co, new_y_co)
