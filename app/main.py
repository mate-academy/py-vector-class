from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector: float | Vector) -> float | Vector:
        if isinstance(vector, Vector):
            return self.x * vector.x + self.y * vector.y
        return Vector(self.x * vector, self.y * vector)

    @staticmethod
    def create_vector_by_two_points(
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length_vector = self.get_length()
        return Vector(
            self.x / length_vector,
            self.y / length_vector
        )

    def angle_between(self, vector: Vector) -> int:
        return round(math.degrees(
            math.acos(
                self.__mul__(vector)
                / (self.get_length() * vector.get_length())
            )
        ))

    def get_angle(self) -> int:
        axis_y = Vector(0, 1)
        return self.angle_between(axis_y)

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        return Vector(
            math.cos(angle) * self.x - math.sin(angle) * self.y,
            math.sin(angle) * self.x + math.cos(angle) * self.y
        )
