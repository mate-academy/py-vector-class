from __future__ import annotations
import math as m


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, object: Vector | int | float) -> Vector | int| float:
        if isinstance(object, Vector):
            return self.x * object.x + self.y * object.y
        else:
            return Vector(self.x * object, self.y * object) 

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        vec1 = Vector(start_point[0], start_point[1])
        vec2 = Vector(end_point[0], end_point[1])
        return vec2 - vec1

    def get_length(self) -> float | int:
        return m.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            normalized_x = self.x / length
            normalized_y = self.y / length
            return Vector(normalized_x, normalized_y)
        else:
            return Vector(0, 0)

    def angle_between(self, vector: Vector) -> int:
        dot_product = self.x * vector.x + self.y * vector.y
        self_mag = self.get_length()
        vector_mag = vector.get_length()
        cos_angle = dot_product / (self_mag * vector_mag)
        angle_deg = m.degrees(m.acos(cos_angle))
        return round(angle_deg)

    def get_angle(self):
        vec = Vector(0, 1)
        return self.angle_between(vec)

    def rotate(self, degrees : int) -> Vector:
        radians = m.radians(degrees)
        new_x = self.x * m.cos(radians) - self.y * m.sin(radians)
        new_y = self.x * m.sin(radians) + self.y * m.cos(radians)
        return Vector(new_x, new_y)
