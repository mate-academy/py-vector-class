from __future__ import annotations
import math


class Vector:

    def __init__(self, x_vector: float, y_vector: float) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if not isinstance(other, Vector):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length_vector = self.get_length()
        return Vector(
            round(self.x / length_vector, 2),
            round(self.y / length_vector, 2)
        )

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        vector_1 = math.sqrt(self.x ** 2 + self.y ** 2)
        vector_2 = math.sqrt(other.x ** 2 + other.y ** 2)
        return round(
            math.degrees(math.acos(dot_product / (vector_1 * vector_2)))
        )

    def get_angle(self) -> float | int:
        if self.x:
            arc_tan = math.atan2(self.x, self.y)
            degrees = math.degrees(arc_tan)
            return round(abs(degrees))
        return self.x

    def rotate(self, angle: int | float) -> Vector:
        radians = math.radians(angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        rotated_x = cos_theta * self.x - sin_theta * self.y
        rotated_y = sin_theta * self.x + cos_theta * self.y
        return Vector(rotated_x, rotated_y)
