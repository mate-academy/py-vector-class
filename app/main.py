from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float, int | float],
            end_point: tuple[int | float, int | float]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> float:
        first_vector_length = self.get_length()
        second_vector_length = vector.get_length()

        mul_vectors = self * vector

        return round(
            math.degrees(
                math.acos(
                    mul_vectors / (first_vector_length * second_vector_length)
                )
            )
        )

    def get_angle(self) -> float:
        vector_2 = Vector(0, abs(self.y))

        return self.angle_between(vector_2)

    def rotate(self, angle: int) -> Vector:
        coordinate_x = (math.cos(math.radians(angle))
                        * self.x - math.sin(math.radians(angle)) * self.y)
        coordinate_y = (math.sin(math.radians(angle)) * self.x
                        + math.cos(math.radians(angle)) * self.y)
        return Vector(coordinate_x, coordinate_y)
