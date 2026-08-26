from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, scalar: Vector | int | float) -> Vector | int | float:
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        elif isinstance(scalar, Vector):
            return self.x * scalar.x + self.y * scalar.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        l1 = self.get_length()
        l2 = vector.get_length()
        if l1 == 0 or l2 == 0:
            return 0
        dot_product = (self.x * vector.x + self.y * vector.y) / (l1 * l2)
        dot_product = max(-1.0, min(1.0, dot_product))
        angle = math.degrees(math.acos(dot_product))
        return int(round(angle))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
