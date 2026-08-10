from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: int | float, y_cord: int | float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float :
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
        else:
            dot_product = Vector(self.x * other, self.y * other)
        return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos((self * other)
                                            / (self.get_length()
                                               * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos((self.y / self.get_length()))))

    def rotate(self, degrees: int) -> Vector:
        a_angle = math.radians(degrees)
        return Vector((self.x * math.cos(a_angle))
                      - (self.y * math.sin(a_angle)),
                      (self.x * math.sin(a_angle))
                      + (self.y * math.cos(a_angle)))
