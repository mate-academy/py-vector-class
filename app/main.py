from __future__ import annotations
import math


class Vector:
    def __init__(self, cord_x: float, cord_y: float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            cord_x=self.x + other.x,
            cord_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            cord_x=self.x - other.x,
            cord_y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(cord_x=self.x * other, cord_y=self.y * other)
        else:
            raise TypeError("Unsupported operand type for multiplication")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x, start_y = start_point
        stop_x, stop_y = end_point
        return cls(cord_x=stop_x - start_x, cord_y=stop_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(rotated_x, rotated_y)
