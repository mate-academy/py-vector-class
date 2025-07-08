from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, multiplier: Vector | int | float) -> Vector | float:
        if isinstance(multiplier, (int, float)):
            return Vector(self.x * multiplier, self.y * multiplier)
        else:
            return self.x * multiplier.x + self.y * multiplier.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cos_a = max(-1,
                    min(1,
                        self.__mul__(vector)
                        / (self.get_length() * vector.get_length())
                        )
                    )
        return round(degrees(acos(cos_a)))

    def get_angle(self,) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        new_x = self.x * cos(radians(degrees)) - self.y * sin(radians(degrees))
        new_y = self.x * sin(radians(degrees)) + self.y * cos(radians(degrees))
        return Vector(new_x, new_y)
