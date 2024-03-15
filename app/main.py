from __future__ import annotations
import math


class Vector:

    def __init__(self, xx: float = 0, yy: float = 0) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            xx=round(self.x + other.x, 2),
            yy=round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            xx=round(self.x - other.x, 2),
            yy=round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(
                xx=self.x * other,
                yy=self.y * other
            )
        else:
            raise TypeError("Unsupported operand type for +=")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            xx=round(self.x * (1 / self.get_length()), 2),
            yy=round(self.y * (1 / self.get_length()), 2)
        )

    def angle_between(self, other: Vector) -> int:
        if self.get_length() == 0 or other.get_length() == 0:
            return 0
        return round(math.degrees(
            (math.acos(
                (self.__mul__(other)
                 / (self.get_length()
                 * other.get_length()))))))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            xx=self.x * math.cos(radians) - self.y * math.sin(radians),
            yy=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
