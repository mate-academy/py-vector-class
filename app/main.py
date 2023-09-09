from __future__ import annotations
from math import sqrt, cos, sin, acos, degrees, atan2, radians


class Vector:
    def __init__(
            self,
            x_cord: int | float,
            y_cord: int | float
    ) -> None:
        self.x_cord = round(x_cord, 2)
        self.y_cord = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            (self.x_cord + other.x_cord),
            (self.y_cord + other.y_cord)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            (self.x_cord - other.x_cord),
            (self.y_cord - other.y_cord)
        )

    def __mul__(self, other: Vector) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(
                self.x_cord * other,
                self.y_cord_cord * other
            )
        else:
            return self.x_cord * other.x_cord + self.y_cord_cord * other.y_cord

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return cls(
            (end_point[0] - start_point[0]),
            (end_point[1] - start_point[1])
        )

    def get_length(self) -> int | float:
        return sqrt(self.x_cord ** 2 + self.y_cord ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            (self.x_cord / self.get_length()),
            (self.y_cord / self.get_length())
        )

    def angle_between(self, other: Vector) -> float:
        # θ = arccos((A · B) / (||A|| * ||B||))
        dot_prod = (self.x_cord * other.x) + (self.y_cord * other.y)
        scalar = self.get_length() * other.get_length()
        angle_radians = acos(dot_prod / scalar)
        return round(degrees(angle_radians))

    def get_angle(self) -> float:
        return abs(round(degrees(atan2(self.x_cord, self.y_cord))))

    def rotate(self, degr: int | float) -> Vector:
        theta = radians(degr)
        x_point = self.x_cord * cos(theta) - self.y_cord * sin(theta)
        y_point = self.x_cord * sin(theta) + self.y_cord * cos(theta)

        return Vector(x_point, y_point)
