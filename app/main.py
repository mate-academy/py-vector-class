from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector: int | Vector) -> Vector | int:
        if isinstance(vector, Vector):
            return self.x * vector.x + self.y * vector.y
        return Vector(round((self.x * vector), 2), round((self.y * vector), 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> float | int:
        dot_product = self * vector
        magnitude = self.get_length() * vector.get_length()
        return round(math.degrees(math.acos(dot_product / magnitude)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        vector_x = (self.x * math.cos(math.radians(degrees))
                    - self.y * math.sin(math.radians(degrees)))
        vector_y = (self.x * math.sin(math.radians(degrees))
                    + self.y * math.cos(math.radians(degrees)))
        return Vector(vector_x, vector_y)
