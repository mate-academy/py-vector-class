from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x + round(other.x, 2),
            point_y=self.y + round(other.y, 2),
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x - round(other.x, 2),
            point_y=self.y - round(other.y, 2),
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                point_x=round(self.x * other, 2),
                point_y=round(self.y * other, 2),
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Vector) -> int:
        return round(math.degrees(math.acos(
            (self.__mul__(vector))
            / (self.get_length() * vector.get_length())
        )))

    def get_angle(self: Vector) -> int:
        positive_y_axis = Vector(0, 1)
        return round(self.angle_between(positive_y_axis))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x2 = math.cos(radians) * self.x - math.sin(radians) * self.y
        y2 = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(x2, y2)
