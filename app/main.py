from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        new_vector_x = self.x + other.x
        new_vector_y = self.y + other.y
        return Vector(new_vector_x, new_vector_y)

    def __sub__(self, other: Vector) -> Vector:
        new_vector_x = self.x - other.x
        new_vector_y = self.y - other.y
        return Vector(new_vector_x, new_vector_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            mul_result = (self.x * other.x) + (self.y * other.y)
            return mul_result
        new_vector_x = self.x * other
        new_vector_y = self.y * other
        return Vector(new_vector_x, new_vector_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        new_vector_x = end_point[0] - start_point[0]
        new_vector_y = end_point[1] - start_point[1]
        return Vector(new_vector_x, new_vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other_vector: Vector) -> int:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        magnitude_product = self.get_length() * other_vector.get_length()

        if magnitude_product == 0:
            return 0
        cos_theta = dot_product / magnitude_product
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_rotated_x, new_rotated_y)
