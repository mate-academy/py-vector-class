from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float | int:
        if isinstance(other, float | int):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float | int],
            end_point: tuple[float | int]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        vectors = self * other
        len_vectors = self.get_length() * other.get_length()
        angle = math.acos(vectors / len_vectors)
        return int(round(math.degrees(angle)))

    def get_angle(self) -> int:
        return abs(int(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        sin = math.sin(radians)
        cos = math.cos(radians)
        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos
        return Vector(new_x, new_y)
