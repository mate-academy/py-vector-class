from __future__ import annotations
import math


class Vector:

    def __init__(self: "Vector", x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: float) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: float) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                f"Unsupported operand type(s) "
                f"for *: 'Vector' and '{type(other).__name__}'"
            )

    def __truediv__(self, scalar: float) -> "Vector":
        return Vector(self.x / scalar, self.y / scalar)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        res = cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )
        return res

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return self / length

    def angle_between(self, other: "Vector") -> float:
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            return 0

        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1, min(1, cos_theta))

        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_theta = self.y / length
        cos_theta = max(-1, min(1, cos_theta))
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: float) -> "Vector":
        rad = math.radians(degrees)
        new_x = round(self.x * math.cos(rad) - self.y * math.sin(rad), 2)
        new_y = round(self.x * math.sin(rad) + self.y * math.cos(rad), 2)
        return Vector(new_x, new_y)
