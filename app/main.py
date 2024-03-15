from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)
    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=round(self.x + other.x, 2),
            y=round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=round(self.x - other.x, 2),
            y=round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        else:
            raise TypeError("Unsupported operand type for +=")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - end_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**(1/2)

    def get_normalized(self) -> Vector:
        return Vector(
            x=round(self.x * (1/self.get_length()), 2),
            y=round(self.y * (1/self.get_length()), 2)
        )

    def angle_between(self, other: Vector) -> int:
        if self.get_length() == 0 or other.get_length() == 0:
            return 0
        return round(math.degrees(
            (math.acos(
                (self.__mul__(other) / self.get_length()
                 * other.get_length())))))

    def get_angle(self):
        pass

    def rotate(self):
        pass

