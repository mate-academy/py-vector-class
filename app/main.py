from __future__ import annotations
import math


class Vector:
    def __init__(self, ax: float | int, ay: int | float) -> None:
        self.x = round(ax, 2)
        self.y = round(ay, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, number: int | float | Vector) -> Vector | int | float:
        if isinstance(number, Vector):
            return self.x * number.x + self.y * number.y
        return Vector(self.x * number, self.y * number)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return pow(pow(self.x, 2) + pow(self.y, 2), 0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        mul_vectors = self * vector

        length_vectors = self.get_length() * vector.get_length()
        angle = math.degrees(math.acos(mul_vectors / length_vectors))

        return round(angle)

    def get_angle(self) -> int:
        radians = math.atan2(self.y, self.x)
        deg = 90 - math.degrees(radians)
        deg = (deg + 360) % 360
        deg = round(deg)
        return deg if deg == 0 else 360 - deg

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        sin = math.sin(radians)
        cos = math.cos(radians)
        ax = self.x * cos - self.y * sin
        ay = self.x * sin + self.y * cos
        return Vector(ax, ay)
