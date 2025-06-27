from __future__ import annotations

import math


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        raise TypeError(
            f"unsupported operand type(s) for +: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        raise TypeError(
            f"unsupported operand type(s) for -: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        raise TypeError(
            f"unsupported operand type(s) for *: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'"
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            cosine = (self * other) / (self.get_length() * other.get_length())
            angle = math.degrees(math.acos(cosine))
            return round(angle)
        raise TypeError(
            f"unsupported operation for '{other.__class__.__name__}'"
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rads = math.radians(degrees)
        return Vector(
            math.cos(rads) * self.x - math.sin(rads) * self.y,
            math.sin(rads) * self.x + math.cos(rads) * self.y
        )
