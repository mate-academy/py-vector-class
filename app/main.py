from __future__ import annotations

class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float):
        self.x = x_coordinate
        self.y = y_coordinate

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + other.x,
            y_coordinate=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - other.x,
            y_coordinate=self.y - other.y
        )