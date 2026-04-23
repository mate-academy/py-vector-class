from __future__ import annotations


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = vector_x
        self.y = vector_y

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> Vector:
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
