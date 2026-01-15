from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 14)
        raise TypeError("Unsupported operation")

    def __rmul__(self, other: float | int) -> Vector:
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> float:
        if self.x == 0 and self.y == 0:
            raise ValueError("Cannot calculate angle for zero vector")
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")

        cos_theta = dot_product / (len_self * len_other)
        cos_theta = max(min(cos_theta, 1), -1)

        angle_rad = math.acos(cos_theta)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
