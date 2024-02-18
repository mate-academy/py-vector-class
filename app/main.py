from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: float | int) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: float | int) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: float,
            end_point: float) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_x = self.x / self.get_length()
        vector_y = self.y / self.get_length()
        return Vector(vector_x, vector_y)

    def angle_between(self, vector: Vector) -> float:
        vector_mul = self.__mul__(vector)
        len_v1 = self.get_length()
        len_v2 = vector.get_length()
        cos_a = vector_mul / (len_v1 * len_v2)
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        return int(abs(angle))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        return Vector(
            self.x * math.cos(angle) - self.y * math.sin(angle),
            self.x * math.sin(angle) + self.y * math.cos(angle)
        )

    # write your code here
    pass
