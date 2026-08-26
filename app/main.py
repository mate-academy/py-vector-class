from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            x_coord=self.x / vector_length,
            y_coord=self.y / vector_length
        )

    def angle_between(self, vector_2: Vector) -> int:
        dot_prod1 = math.sqrt(self.x ** 2 + self.y ** 2)
        dot_prod2 = math.sqrt(vector_2.x ** 2 + vector_2.y ** 2)
        sum_of_vectors = self.x * vector_2.x + self.y * vector_2.y
        cos_a = sum_of_vectors / (dot_prod1 * dot_prod2)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vector_dot_product = math.sqrt(self.x ** 2 + self.y ** 2)
        cos_a = (self.x * 0 + self.y * 1) / vector_dot_product
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        new_y = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(
            x_coord=new_x,
            y_coord=new_y
        )
