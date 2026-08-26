from __future__ import annotations
from math import sqrt, cos, sin, radians, acos, degrees


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            # Dot product formula - a · b = ax × bx + ay × by
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"Unsupported type for multiplication: "
                            f"{type(other)}. Must be int, float or Vector.")

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        # Vector by two points - x2−x1, y2−y1
        return cls(
            end[0] - start[0],
            end[1] - start[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        # Normalized vector formula - (x/len, y/len)
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        # formula - arc cos(dot product / (lenA * lenB))
        angle = degrees(acos(
            (self * other / (self.get_length() * other.get_length()))
        ))
        return round(angle)

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, num: int | float) -> Vector:
        return Vector(
            self.x * cos(radians(num)) - self.y * sin(radians(num)),
            self.x * sin(radians(num)) + self.y * cos(radians(num))
        )
