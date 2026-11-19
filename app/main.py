from __future__ import annotations
import math


class Vector:
    vector = []

    def __init__(self, x_coordinate: int | float, y_coordinate: int | float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)
        Vector.vector.append(self)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_coordinate + other.x_coordinate, self.y_coordinate + other.y_coordinate)

    def __sub__(self, other: Vector) -> Vector:
        isinstance(other, Vector)
        return Vector(self.x_coordinate - other.x_coordinate, self.y_coordinate - other.y_coordinate)

    def __mul__(self, other: "Vector | int | float") -> Vector | float:
        if isinstance(other, Vector):
            return self.x_coordinate * other.x_coordinate + self.y_coordinate * other.y_coordinate
        return Vector(self.x_coordinate * other, self.y_coordinate * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x_coordinate ** 2 + self.y_coordinate ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x_coordinate / self.get_length(), self.y_coordinate / self.get_length())

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x_coordinate * other.x_coordinate + self.y_coordinate * other.y_coordinate
        length_product = self.get_length() * other.get_length()
        cos_a = dot_product / length_product
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x_coordinate * math.cos(radians) - self.y_coordinate * math.sin(radians)
        new_y = self.x_coordinate * math.sin(radians) + self.y_coordinate * math.cos(radians)
        return Vector(new_x, new_y)
