from __future__ import annotations


class Vector:
    def __init__(self, x: int | float = 0, y: int | float = 0) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
    
    @classmethod
    def create_vector_by_two_points(cls, point1: tuple[int | float, int | float], point2: tuple[int | float, int | float]) -> Vector:
        return cls(point2[0] - point1[0], point2[1] - point1[1])
    
    def get_length(self) -> float:
        pass

    def get_normalized(self) -> Vector:
        pass

    def angle_between(self, other: Vector) -> float:
        pass

    def rotate(self, angle: float) -> Vector:
        pass
