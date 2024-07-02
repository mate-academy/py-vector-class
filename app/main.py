from __future__ import annotations
import math


class Vector:
    def __init__(self, axis_x: float | int, axis_y: float | int) -> None:
        self.axis_x = round(axis_x, 2)
        self.axis_y = round(axis_y, 2)

    def __add__(self, other: int | float) -> int | float:
        return Vector(
            (self.axis_x + other.axis_x),
            (self.axis_y + other.axis_y)
        )

    def __sub__(self, other: int | float) -> int | float:
        return Vector(
            (self.axis_x - other.axis_x),
            (self.axis_y - other.axis_y)
        )

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.axis_x * other, self.axis_y * other)
        elif isinstance(other, Vector):
            return self.axis_x * other.axis_x + self.axis_y * other.axis_y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        point_list = []
        for point in range(len(start_point)):
            point_list.append(end_point[point] - start_point[point])

        axis_x = point_list[0]
        axis_y = point_list[1]

        return cls(axis_x, axis_y)

    def get_length(self) -> Vector:
        return math.sqrt(self.axis_x ** 2 + self.axis_y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.axis_x / self.get_length(),
            self.axis_y / self.get_length()
        )

    def angle_between(
            self,
            other: int | float | Vector
    ) -> int | float | Vector:
        if isinstance(other, Vector):
            dot_product = self * other
            len_self = self.get_length()
            len_other = other.get_length()
            if len_self or len_other:
                cos_angle = dot_product / (len_self * len_other)
                cos_angle = max(-1.0, min(1.0, cos_angle))
                return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int | float) -> int | float:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        new_x = round((self.axis_x * cos) - (self.axis_y * sin), 2)
        new_y = round((self.axis_x * sin) + (self.axis_y * cos), 2)
        return Vector(new_x, new_y)
