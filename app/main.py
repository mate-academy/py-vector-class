from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand type(s) for +: 'Vector' and {type(other)}")

        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand type(s) for +: 'Vector' and {type(other)}")

        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float | int:
        if not isinstance(other, (Vector, float, int)):
            raise TypeError(f"unsupported operand type(s) for +: 'Vector'|'float'|'int' and {type(other)}")

        if isinstance(other, (float, int)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        if not isinstance(other, Vector):
            raise TypeError(f"unsupported operand type(s) for +: 'Vector' and {type(other)}")

        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_vect = Vector(
            x=0,
            y=1
        )
        return self.angle_between(y_vect)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x=self.x * math.cos(radians) - self.y * math.sin(radians),
            y=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
