from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector | float:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                "Multiplication is allowed only with int, float, or Vector"
            )

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

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        scalar_mul = Vector.__mul__(self, other)
        lengh_self = self.get_length()
        lengh_other = other.get_length()
        cos_a = scalar_mul / (lengh_self * lengh_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        sin_d = math.sin(math.radians(degrees))
        cos_d = math.cos(math.radians(degrees))
        new_x = round((self.x * cos_d) - (self.y * sin_d), 2)
        new_y = round((self.x * sin_d) + (self.y * cos_d), 2)
        return Vector(new_x, new_y)
