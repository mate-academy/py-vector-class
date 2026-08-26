from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        unit_vector = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector((self.x / unit_vector), (self.y / unit_vector))

    def angle_between(self, other: Vector) -> float:
        length_vector_1 = self.get_length()
        length_vector_2 = other.get_length()
        mul_vectors = self * other
        return round(math.degrees(
            math.acos(mul_vectors / (length_vector_1 * length_vector_2))))

    def get_angle(self) -> float:
        vector_2 = Vector(0, abs(self.y))
        angel = self.angle_between(vector_2)
        return angel

    def rotate(self, angle: int) -> Vector:
        coordinate_x = (math.cos(math.radians(angle)) * self.x
                        - math.sin(math.radians(angle)) * self.y)
        coordinate_y = (math.sin(math.radians(angle)) * self.x
                        + math.cos(math.radians(angle)) * self.y)
        return Vector(coordinate_x, coordinate_y)
