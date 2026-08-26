from __future__ import annotations
import math


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int | float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"unsupported operand type (s) for *: /n "
                            f"Vector and {type(other)}")

    @classmethod
    def create_vector_by_two_points(cls, star_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - star_point[0],
                   end_point[1] - star_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees
                     (math.acos(((self.x * other.x)
                                 + (self.y * other.y))
                                / (self.get_length() * other.get_length()))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        rotated_x = self.x * math.cos(angle) - self.y * math.sin(angle)
        rotated_y = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(rotated_x, rotated_y)
