from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: float | int | Vector) -> Vector | int:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        res1 = end_point[0] - start_point[0]
        res2 = end_point[1] - start_point[1]
        return Vector(res1, res2)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        angle = (self.__mul__(other)
                 / (self.get_length()
                    * other.get_length()))
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        angle = (self.__mul__(positive_y)
                 / (self.get_length()
                    * positive_y.get_length()))
        return round(math.degrees(math.acos(angle)))

    def rotate(self, degrees: int) -> Vector:
        radianss = math.radians(degrees)
        return Vector(self.x * math.cos(radianss) - self.y * math.sin(radianss),
                      self.x * math.sin(radianss) + self.y * math.cos(radianss))
