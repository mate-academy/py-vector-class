from __future__ import annotations
import math


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + float(other), self.y + float(other))
        else:
            raise Exception(
                "Unsupported operand type."
                " You can only add two vectors or a scalar."
            )

    def __sub__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - float(other), self.y - float(other))
        else:
            raise Exception(
                "Unsupported operand type."
                " You can only add two vectors or a scalar."
            )

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise Exception(
                "Unsupported operand type."
                " You can only add two vectors or a scalar."
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = round(
            self.x
            * math.cos(radians)
            - self.y
            * math.sin(radians),
            2)
        new_y = round(
            self.x
            * math.sin(radians)
            + self.y
            * math.cos(radians),
            2)
        return Vector(new_x, new_y)
