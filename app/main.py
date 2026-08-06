from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self.__mul__(other)
        magnitude_product = self.get_length() * other.get_length()
        cos_a = dot_product / magnitude_product
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return round(self.angle_between(y_axis))

    def rotate(self, degrees: int) -> Vector:
        deg_to_rad = math.radians(degrees)
        x_prime = self.x * math.cos(deg_to_rad) - self.y * math.sin(deg_to_rad)
        y_prime = self.x * math.sin(deg_to_rad) + self.y * math.cos(deg_to_rad)
        return Vector(round(x_prime, 2), round(y_prime, 2))
