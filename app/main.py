from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x_coord + vector.x_coord, self.y_coord + vector.y_coord)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x_coord - vector.x_coord, self.y_coord - vector.y_coord)

    def __mul__(self, multiplier: Vector | int | float) -> Vector | float:
        if isinstance(multiplier, (int, float)):
            return Vector(self.x_coord * multiplier, self.y_coord * multiplier)
        else:
            return self.x_coord * multiplier.x_coord + self.y_coord * multiplier.y_coord

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x_coord / self.get_length(), self.y_coord / self.get_length())

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
        new_x = self.x_coord * cos(radians(degrees)) - self.y_coord * sin(radians(degrees))
        new_y = self.x_coord * sin(radians(degrees)) + self.y_coord * cos(radians(degrees))
        return Vector(new_x, new_y)
