from __future__ import annotations
import math


class Vector:
    def __init__(self,
                 x_point: int | float,
                 y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x + other.x, y_point=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_point=self.x - other.x, y_point=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(x_point=self.x * other, y_point=self.y * other)
        return self.dot_product(other)

    def dot_product(self, other: Vector) -> float | int:
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(x_point=end_point[0] - start_point[0],
                   y_point=end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return math.sqrt((self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x_point=self.x / length, y_point=self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        dot = self.dot_product(other)
        fist_mag = self.get_length()
        second_mag = other.get_length()
        cos_a = dot / (fist_mag * second_mag)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_vector = Vector(x_point=0, y_point=10)
        return self.angle_between(y_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.x * math.cos(radians)) - (self.y * math.sin(radians))
        new_y = (self.x * math.sin(radians)) + (self.y * math.cos(radians))
        return Vector(x_point=new_x, y_point=new_y)
