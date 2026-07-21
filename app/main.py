from __future__ import annotations
import math


class Vector:
    def __init__(self,
                 x_axis: float,
                 y_axis: float
                 ) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self,
                other: Vector
                ) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self,
                other: Vector | int | float
                ) -> Vector | float:
        if isinstance(other, (int, float, )):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length,
                          self.y / length)

    def angle_between(self,
                      other: Vector
                      ) -> float:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self,
               degrees: float | int
               ) -> Vector:
        radians = math.radians(degrees)
        x_axis = (self.x * math.cos(radians)
                  - self.y * math.sin(radians))
        y_axis = (self.x * math.sin(radians)
                  + self.y * math.cos(radians))
        return Vector(x_axis, y_axis)
