from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_coord + other.x_coord,
                      self.y_coord + other.y_coord)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x_coord - other.x_coord,
                      self.y_coord - other.y_coord)

    def __mul__(self, number: int | float | Vector) -> Vector | float | int:
        if isinstance(number, Vector):
            return self.x_coord * number.x_coord + \
                self.y_coord * number.y_coord

        return Vector(self.x_coord * number, self.y_coord * number)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> int | float:
        return (self.x_coord ** 2 + self.y_coord ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x_coord / self.get_length(),
            self.y_coord / self.get_length(),
        )

    def angle_between(self, other: Vector) -> int:
        prod = self.__mul__(other)
        u_mod = self.get_length()
        v_mod = other.get_length()
        cos_a = prod / (u_mod * v_mod)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        deg = math.radians(degrees)
        rotated_x = self.x_coord * math.cos(deg) - self.y_coord * math.sin(deg)
        rotated_y = self.x_coord * math.sin(deg) + self.y_coord * math.cos(deg)
        return Vector(rotated_x, rotated_y)
