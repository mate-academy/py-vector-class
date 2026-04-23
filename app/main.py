from __future__ import annotations


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other + self.y * other
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: Vector | float) -> Vector | float:
        return Vector(self.x / other.x, self.y / other.y)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
