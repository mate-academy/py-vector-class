from __future__ import annotations
import math
import numbers


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.x = round(end_x, 2)
        self.y = round(end_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))
        raise TypeError("Operand must be an instance of Vector")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))
        raise TypeError("Operand must be an instance of Vector")

    def __mul__(self, other: numbers.Real | Vector) -> float | Vector:
        if isinstance(other, numbers.Real):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Operand must be an instance of Vector or number")

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_a = dot_product / (length_self * length_other)
        cos_a = max(-1.0, min(1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)
