from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x_point = round(x_point, 2)
        self.y_point = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x_point + other.x_point,
            y_point=self.y_point + other.y_point
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x_point - other.x_point,
            y_point=self.y_point - other.y_point
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return ((self.x_point * other.x_point)
                    + (self.y_point * other.y_point))
        return Vector(
            x_point=self.x_point * other,
            y_point=self.y_point * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_point=end_point[0] - start_point[0],
            y_point=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x_point ** 2 + self.y_point ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_point=self.x_point / self.get_length(),
            y_point=self.y_point / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        modul_self = (self.x_point ** 2 + self.y_point ** 2) ** 0.5
        modul_other = (other.x_point ** 2 + other.y_point ** 2) ** 0.5

        cos_a = (self * other) / abs((modul_self * modul_other))
        angle = round(math.degrees(math.acos(cos_a)))

        return angle

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x_point, self.y_point)
        angle_degrees = round(abs(math.degrees(angle_radians)))

        return angle_degrees

    def rotate(self, degrees: int) -> Vector:
        angle_radians = math.radians(degrees)

        new_x = (self.x_point * math.cos(angle_radians)
                 - self.y_point * math.sin(angle_radians))
        new_y = (self.x_point * math.sin(angle_radians)
                 + self.y_point * math.cos(angle_radians))

        return Vector(x_point=new_x, y_point=new_y)
