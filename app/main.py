from __future__ import annotations

import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError(
            f"Unsupported operand type(s) for +: 'Vector' and '{type(other)}'")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError(
            f"Unsupported operand type(s) for -: 'Vector' and '{type(other)}'")

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError(
            f"Unsupported operand type(s) for *: 'Vector' and '{type(other)}'")

    @classmethod
    def create_vector_by_two_points(cls, start_point: (int, int),
                                    end_point: (int, int)) -> Vector:
        """Creates a vector between two points"""
        if not all(isinstance(p, tuple) for p in (start_point, end_point)):
            raise TypeError("start and end must be tuples")
        if len(start_point) != 2 or len(end_point) != 2:
            raise ValueError("start and end must be 2D points")
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        """Returns length of the vector"""
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        """Returns normalized copy of vector"""
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        """Returns angle between current vector and other in degrees"""
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length()))))

    def get_angle(self) -> float:
        """Returns angle between the current vector and positive Y axis"""
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        """Returns a rotated Vector by degrees."""
        radians = math.radians(angle)
        coord_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        coord_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(coord_x, coord_y)
