from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x=(self.x + other.x), y=(self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x=(self.x - other.x), y=(self.y - other.y))

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(
                x=round(self.x * other, 2), y=round(self.y * other, 2)
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0], y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Can't normalize")
        return Vector(x=self.x / length, y=self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        vectors_multiplied = self.get_length() * other.get_length()
        if vectors_multiplied == 0:
            raise ValueError("Vector must have a length")
        return round(math.degrees(math.acos(dot_product / vectors_multiplied)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        cos_theta = math.cos(math.radians(degrees))
        sin_theta = math.sin(math.radians(degrees))
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(x=new_x, y=new_y)
