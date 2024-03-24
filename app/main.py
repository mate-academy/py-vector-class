from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x: float = round(x_coordinate, 2)
        self.y: float = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector or float) -> Vector or float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        scalar = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self != 0 and length_other != 0:
            cosine = scalar / (length_self * length_other)
            degrees = math.degrees(math.acos(cosine))
            return round(degrees)

    def get_angle(self) -> float:
        angle_degrees = math.degrees(math.atan2(self.x, self.y))
        return abs(round(angle_degrees))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return self.__class__(new_x, new_y)
