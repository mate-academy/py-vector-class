from __future__ import annotations

import math


class Vector:
    def __init__(
            self,
            x_cord: float,
            y_cord: float
    ) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x
                    + self.y * other.y)
        else:
            return Vector(self.x * other,
                          self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: float | float,
                                    end_point: float | float) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2
                         + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length,
                      self.y / length)

    def angle_between(self, other: Vector) -> float:
        cos_a = ((self.x * other.x
                  + self.y * other.y)
                 / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.x * math.cos(radians)
                 - self.y * math.sin(radians))
        new_y = (self.x * math.sin(radians)
                 + self.y * math.cos(radians))
        return Vector(round(new_x, 2), round(new_y, 2))
