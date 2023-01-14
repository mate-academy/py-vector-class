from __future__ import annotations
import math


class Vector:
    def __init__(self, _x: int | float, _y: int | float) -> None:
        self.x = round(_x, 2)
        self.y = round(_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / math.fabs(self.get_length()),
                      self.y / math.fabs(self.get_length()))

    def angle_between(self, other: Vector) -> int | float:
        return round(math.degrees(math.acos(((self * other)
                                             / (self.get_length()
                                            * other.get_length())))))

    def get_angle(self) -> int | float:
        new_vector = Vector(0, self.y)
        if self.x < 0 and self.y < 0:
            return 180 - self.angle_between(new_vector)
        else:
            return self.angle_between(new_vector)

    def rotate(self, angle: int | float) -> Vector:
        return Vector(self.x * math.cos(math.radians(angle))
                      - self.y * math.sin(math.radians(angle)),
                      self.x * math.sin(math.radians(angle))
                      + self.y * math.cos(math.radians(angle)))
