from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x, self.y = round(x_coord, 2), round(y_coord, 2)

    def __add__(self, other_vector: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other_vector.x,
            y_coord=self.y + other_vector.y
        )

    def __sub__(self, other_vector: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other_vector.x,
            y_coord=self.y - other_vector.y
        )

    def __mul__(
            self, multiplication: Vector | int | float
    ) -> Vector | int | float:
        if isinstance(multiplication, Vector):
            return self.x * multiplication.x + self.y * multiplication.y
        return Vector(
            x_coord=self.x * multiplication,
            y_coord=self.y * multiplication
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x, y = end_point[0] - start_point[0], end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        current_length = self.get_length()
        return Vector(
            x_coord=self.x / current_length,
            y_coord=self.y / current_length
        )

    def angle_between(self, other_vector: Vector) -> float:
        cosines = (self * other_vector) / (
            self.get_length() * other_vector.get_length()
        )

        return round(math.degrees(math.acos(cosines)), 0)

    def get_angle(self) -> float:
        return int(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int | float) -> Vector:
        angle_radians = math.radians(degrees)

        return Vector(
            x_coord=(self.x * math.cos(angle_radians)
                     - self.y * math.sin(angle_radians)),
            y_coord=(self.x * math.sin(angle_radians)
                     + self.y * math.cos(angle_radians)),
        )
