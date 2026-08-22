from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x : float, coord_y : float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other : Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other : Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other : Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point : tuple[int | float, int | float],
            end_point : tuple[int | float, int | float]) \
            -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / Vector.get_length(self),
                      (self.y / Vector.get_length(self)))

    def angle_between(self, vector1 : Vector) -> int:
        return (round(math.degrees(math.acos(
            (vector1.x * self.x + vector1.y * self.y)
            / (((vector1.x ** 2 + vector1.y ** 2) ** 0.5)
                * ((self.x ** 2 + self.y ** 2) ** 0.5))))))

    def get_angle(self) -> int:
        vis_y = Vector(0, 1)
        return self.angle_between(vis_y)

    def rotate(self, degrees : int) -> Vector:
        try_degrees = math.radians(degrees)
        new_x = self.x * math.cos(try_degrees) - self.y * math.sin(try_degrees)
        new_y = self.x * math.sin(try_degrees) + self.y * math.cos(try_degrees)
        return Vector(new_x, new_y)
