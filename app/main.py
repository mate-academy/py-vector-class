from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coor=self.x + other.x,
            y_coor=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coor=self.x - other.x,
            y_coor=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(
                x_coor=self.x * other,
                y_coor=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_coor=end_point[0] - start_point[0],
            y_coor=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x_coor=self.x / length,
            y_coor=self.y / length
        )

    def angle_between(self, vector: Vector) -> int:
        cos_of_the_angle = ((self.x * vector.x + self.y * vector.y)
                            / (self.get_length() * vector.get_length()))
        angel = math.degrees(math.acos(cos_of_the_angle))
        return round(angel)

    def get_angle(self) -> int:
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_coor=math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,
            y_coor=math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y
        )
