from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector: Vector | float) -> Vector | float:
        if isinstance(vector, Vector):
            return self.x * vector.x + self.y * vector.y
        else:
            return Vector(self.x * vector, self.y * vector)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        angle = math.degrees(math.acos(
            (self * vector) / (self.get_length() * vector.get_length())
        ))
        return round(angle)

    def get_angle(self) -> int:
        vector = Vector(0, 1)
        return self.angle_between(vector)

    def rotate(self, degrees: float) -> Vector:
        degrees = math.radians(degrees)

        return Vector(
            math.cos(degrees) * self.x - math.sin(degrees)
            * self.y,
            math.sin(degrees) * self.x + math.cos(degrees)
            * self.y
        )
