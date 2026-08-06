from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return (Vector(self.x + other.x,
                       self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return (Vector(self.x - other.x,
                       self.y - other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            mul = (self.x * other.x) + (self.y * other.y)
            return mul
        return (Vector(round((self.x * other), 2),
                       round((self.y * other), 2)))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        normalized_x = self.x / vector_length
        normalized_y = self.y / vector_length
        return Vector(round(normalized_x, 2), round(normalized_y, 2))

    def angle_between(self, other: Vector) -> float | int:
        dot_product = (self.x * other.x) +\
                      (self.y * other.y)
        mag1 = self.get_length()
        mag2 = other.get_length()
        return round(math.degrees(math.acos(dot_product / (mag1 * mag2))))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            x_coordinate=(math.cos(degrees) * self.x) - (math.sin(degrees)
                                                         * self.y),
            y_coordinate=(math.sin(degrees) * self.x) + (math.cos(degrees)
                                                         * self.y)
        )
