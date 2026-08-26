from __future__ import annotations

from math import sin, cos, acos, atan2, degrees, radians


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        magnitude = self.get_length() * other.get_length()
        return round(degrees(acos(dot_product / magnitude)))

    def get_angle(self) -> float:
        angle = degrees(atan2(self.x, self.y))
        return round(abs(angle))

    def rotate(self, degrees_: float) -> Vector:
        original_x = self.x
        original_y = self.y
        rotated_x = (original_x * cos(radians(degrees_))
                     - original_y * sin(radians(degrees_)))
        rotated_y = (original_x * sin(radians(degrees_))
                     + original_y * cos(radians(degrees_)))
        return Vector(rotated_x, rotated_y)
