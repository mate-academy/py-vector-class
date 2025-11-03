from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other : Vector) -> Vector:
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(x=self.x * other,
                      y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(x=end_point[0] - start_point[0],
                   y=end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x=self.x / length,
                      y=self.y / length)

    def angle_between(self, vector: Vector) -> int:
        cos_a = self * vector / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(x=self.x * math.cos(radians)
                      - self.y * math.sin(radians),
                      y=self.x * math.sin(radians)
                      + self.y * math.cos(radians))
vector1 = Vector(2, 4)
vector2 = vector1 * 3.743
print(isinstance(vector2, Vector)) #