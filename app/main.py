from __future__ import annotations

import math


class Vector:

    def __init__(self, latitude: float, longitude: float) -> None:
        self.x = round(latitude, 2)
        self.y = round(longitude, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            result = (self.x * other.x) + (self.y * other.y)
            return result
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        start_vector = Vector(start[0], start[1])
        end_vector = Vector(end[0], end[1])
        return end_vector - start_vector

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        point = self.__mul__(other)
        length = self.get_length() * other.get_length()
        angle = max(-1, min(1, point / length))
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        point = (self.y ** 2)
        length = self.get_length() * math.sqrt(self.y ** 2)
        cos_degrees = max(-1, min(1, point / length))
        if self.y < 0:
            degrees = 180 - round(math.degrees(math.acos(cos_degrees)))
        else:
            degrees = round(math.degrees(math.acos(cos_degrees)))
        return degrees

    def rotate(self, degrees: int) -> Vector:
        cos_degrees = math.cos(math.radians(degrees))
        sin_degrees = math.sin(math.radians(degrees))
        latitude = self.x * cos_degrees - self.y * sin_degrees
        longitude = self.x * sin_degrees + self.y * cos_degrees
        return Vector(latitude, longitude)
