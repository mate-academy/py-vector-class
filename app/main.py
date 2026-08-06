from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector | int:
        if isinstance(other, Vector):
            result = self.x * other.x + self.y * other.y
        else:
            result = Vector(self.x * other,
                            self.y * other)
        return result

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) \
            -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1]
                   )

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self: Vector) -> Vector:
        if self.get_length() == 0:
            return self
        else:
            return Vector(round((self.x / self.get_length()), 2),
                          round((self.y / self.get_length()), 2))

    def angle_between(self, vector: tuple) -> int:
        if isinstance(vector, Vector):
            angle = Vector.__mul__(self, vector) / \
                (Vector.get_length(self) * Vector.get_length(vector))
            return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        return int(
            math.degrees(math.acos(
                self.y / ((self.x ** 2 + self.y ** 2) ** 0.5)))
        )

    def rotate(self, degrees: int) -> Vector:
        return Vector(self.x * math.cos(math.radians(degrees))
                      - self.y * math.sin(math.radians(degrees)),
                      self.y * math.cos(math.radians(degrees))
                      + self.x * math.sin(math.radians(degrees)))
