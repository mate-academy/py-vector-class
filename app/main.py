from __future__ import annotations
from math import sqrt, cos, sin, acos, degrees, radians


class Vector:
    def __init__(self, x_param: float, y_param: float) -> None:
        self.x = round(x_param, 2)
        self.y = round(y_param, 2)

    def __add__(self, rho: Vector) -> Vector:
        return Vector(self.x + rho.x, self.y + rho.y)

    def __sub__(self, rho: Vector) -> Vector:
        return Vector(self.x - rho.x, self.y - rho.y)

    def __mul__(self, rho: float | Vector) -> float | Vector:
        if isinstance(rho, float) or rho == 0:
            return Vector(self.x * rho, self.y * rho)
        if isinstance(rho, Vector):
            return self.x * rho.x + self.y * rho.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float],
        end_point: tuple[float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        if (magnitude_product := self.get_length() * vector.get_length()):
            return round(degrees(acos(self * vector / magnitude_product)), 0)
        return 0.0

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle_degrees: int) -> Vector:
        angle_radians = radians(angle_degrees)
        return Vector(
            self.x * cos(angle_radians) - self.y * sin(angle_radians),
            self.x * sin(angle_radians) + self.y * cos(angle_radians)
        )
