from __future__ import annotations
import math


class Vector:
    def __init__(self, co_x: (float, int), co_y: (float, int)) -> None:
        self.x = round(co_x, 2)
        self.y = round(co_y, 2)

    def __add__(self: Vector, other: Vector) -> Vector:
        self.add_x = self.x + other.x
        self.add_y = self.y + other.y
        return Vector(self.add_x, self.add_y)

    def __sub__(self: Vector, other: Vector) -> Vector:
        self.sub_x = self.x - other.x
        self.sub_y = self.y - other.y
        return Vector(self.sub_x, self.sub_y)

    def __mul__(self: Vector, other: (Vector, float, int)) \
            -> (Vector, float, int):
        if isinstance(other, Vector):
            self.mul_vectors = self.x * other.x + self.y * other.y
            return self.mul_vectors
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self: Vector) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self: Vector) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self: Vector, other: Vector) -> int:
        cos_a = (
                (self.x * other.x + self.y * other.y)
            / (math.sqrt(self.x ** 2 + self.y ** 2)
                * math.sqrt(other.x ** 2 + other.y ** 2))
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self: Vector) -> int:
        other = Vector(0, 100)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        return Vector(self.x * math.cos(rad) - self.y * math.sin(rad),
                      self.x * math.sin(rad) + self.y * math.cos(rad))
