from typing import Tuple
from math import sqrt, degrees, radians, acos, cos, sin


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> None:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> None:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: "Vector") -> None:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> "Vector":
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        magnitude = self.get_length()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        norm_x = self.x / magnitude
        norm_y = self.y / magnitude
        return Vector(norm_x, norm_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        magnitude_a = self.get_length()
        magnitude_b = other.get_length()
        if magnitude_a == 0 or magnitude_b == 0:
            raise ValueError("Cannot calculate angle with zero-length vector.")
        cos_theta = dot_product / (magnitude_a * magnitude_b)
        return round(degrees(acos(cos_theta)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, rotation_degrees: int) -> None:
        rotation_radians = radians(rotation_degrees)
        x_point = (
            self.x * cos(rotation_radians) - self.y * sin(rotation_radians)
        )
        y_point = (
            self.x * sin(rotation_radians) + self.y * cos(rotation_radians)
        )
        return Vector(round(x_point, 2), round(y_point, 2))
