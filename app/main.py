from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> callable:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, Vector):
            res = self.x * other.x + self.y * other.y
            return res
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        res = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        return res

    def get_normalized(self) -> callable:
        length = self.get_length()
        return Vector(
            x=self.x / length,
            y=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        length = self.get_length() * other.get_length()
        cos = (self * other) / length
        angle = math.degrees(math.acos(cos))
        return round(angle, 0)

    def get_angle(self) -> int:
        tan = self.x / self.y
        if tan == 0:
            if self.y > 0:
                return 0
            else:
                return 180
        elif tan < 0:
            angle = abs(math.degrees(math.atan(tan)))
        else:
            angle = 180 - math.degrees(math.atan(tan))
        return round(angle)

    def rotate(self, rot_ang: int) -> Vector:
        rot_ang_rad = math.radians(rot_ang)
        new_x = math.cos(rot_ang_rad) * self.x - math.sin(rot_ang_rad) * self.y
        new_y = math.sin(rot_ang_rad) * self.x + math.cos(rot_ang_rad) * self.y
        new_x = round(new_x, 2)
        new_y = round(new_y, 2)
        return Vector(
            x=new_x,
            y=new_y
        )
