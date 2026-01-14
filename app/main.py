from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        vec3 = Vector(self.x + other.x, self.y + other.y)
        return vec3

    def __sub__(self, other: Vector) -> Vector:
        vec3 = Vector(self.x - other.x, self.y - other.y)
        return vec3

    def __mul__(self, other: int | float) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            vec3 = Vector(self.x * other, self.y * other)
            return vec3

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        vec = (Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1]))
        return vec

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        vec = Vector(self.x / length, self.y / length)
        return vec

    def angle_between(self, vector: Vector) -> int:
        dot = self.x * vector.x + self.y * vector.y
        cos_a = dot / (self.get_length() * vector.get_length())
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, angle: int | float) -> Vector:
        angle = math.radians(angle)
        dot_x = self.x * math.cos(angle) - self.y * math.sin(angle)
        dot_y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(dot_x, dot_y)
