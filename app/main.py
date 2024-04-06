from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_argument: int | float,
            y_argument: int | float
    ) -> None:
        self.x = round(x_argument, 2)
        self.y = round(y_argument, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        multiply = self * other
        divider = (math.sqrt(self.x ** 2 + self.y ** 2)
                   * math.sqrt(other.x ** 2 + other.y ** 2))
        alpha = multiply / divider
        return round(math.degrees(math.acos(alpha)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        rotated_x = (self.x * math.cos(math.radians(degrees))
                     - self.y * math.sin(math.radians(degrees)))
        rotated_y = (self.x * math.sin(math.radians(degrees))
                     + self.y * math.cos(math.radians(degrees)))
        return Vector(rotated_x, rotated_y)
