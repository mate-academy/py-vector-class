from __future__ import division, annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None: # noqa
        self.x = round(x, 2)
        self.y = round(y, 2)

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

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x_coordinate = round((self.x / length), 2)
        y_coordinate = round((self.y / length), 2)
        return Vector(x_coordinate, y_coordinate)

    def angle_between(self, other: Vector) -> int:
        length = self.x * other.x + self.y * other.y
        modul_x = math.sqrt(self.x ** 2 + self.y ** 2)
        modul_other = math.sqrt(other.x ** 2 + other.y ** 2)
        angle = length / (modul_x * modul_other)
        angle_in_degrees = math.degrees(math.acos(angle))
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        modul = self.get_length()
        return round(math.degrees(math.acos(self.y / modul)))

    def rotate(self, angle: float) -> Vector:
        new_angle = math.radians(angle)
        x_coord = self.x * math.cos(new_angle) - self.y * math.sin(new_angle)
        y_coord = self.x * math.sin(new_angle) + self.y * math.cos(new_angle)
        return Vector(x_coord, y_coord)
