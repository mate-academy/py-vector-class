from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        # P2 - P1 = (x2 - x1, y2 - y1)
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def __add__(self, other: Vector) -> Vector:
        # V3 = (x1 + x2, y1 + y2)
        return (
            Vector(self.x + other.x, self.y + other.y)
            if isinstance(other, Vector)
            else "You can only add another Vector to this Vector"
        )

    def __sub__(self, other: Vector) -> Vector:
        # V3 = (x1 - x2, y1 - y2)
        return (
            Vector(self.x - other.x, self.y - other.y)
            if isinstance(other, Vector)
            else "You can only subtract another Vector from this Vector"
        )

    def __mul__(self, other: float | Vector) -> Vector | float:
        # A · B = x1x2 + y1y2
        return (
            (self.x * other.x) + (self.y * other.y)
            if isinstance(other, Vector)
            else Vector(round(self.x * other, 2), round(self.y * other, 2))
        )

    def get_length(self) -> float:
        # ||v|| = sqrt(x² + y²)
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        #  v_norm = (x/||v|| , y/||v||)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        # cos(θ) = (a·b) / (||a|| * ||b||)
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        # new_x = x * cos(θ) - y * sin(θ)
        # new_y = x * sin(θ) + y * cos(θ)
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)


vector = Vector(-4.44, 5.2)
print(vector.get_length())
