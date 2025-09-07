from __future__ import annotations

class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float):
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

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

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                x_coordinate=self.x * other,
                y_coordinate=self.y * other
            )
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            x_coordinate=end_point[0] - start_point[0],
            y_coordinate=end_point[1] - start_point[1]
        )
