from __future__ import annotations
import math


class Vector:
    
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector | float | int) -> Vector:
        vector = Vector(self.x + other.x, self.y + other.y)
        if isinstance(vector, Vector):
            return vector

    def __sub__(self, other: Vector | float | int) -> Vector:
        vector = Vector(self.x - other.x, self.y - other.y)
        if isinstance(vector, Vector):
            return vector

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        angle_degrees = math.degrees(math.acos(cos_a))
        return round(angle_degrees)

    def get_angle(self) -> int:
        return round(math.acos(self.y / self.get_length()) * (180 / math.pi))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
