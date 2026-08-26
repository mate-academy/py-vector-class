from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self. x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: Vector,
            end_point: Vector
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        return round(math.degrees(math.acos(
            self.__mul__(vector) / (self.get_length() * vector.get_length()))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            math.cos(radians) * self.x - math.sin(radians) * self.y,
            math.sin(radians) * self.x + math.cos(radians) * self.y
        )
