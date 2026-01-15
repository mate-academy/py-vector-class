from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | Vector) -> Vector | int:
        if isinstance(other, int | float):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x = start_point[0]
        start_y = start_point[1]
        end_x = end_point[0]
        end_y = end_point[1]
        return cls(
            x_coord=end_x - start_x,
            y_coord=end_y - start_y
        )

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            x_coord=round(self.x / length, 2),
            y_coord=round(self.y / length, 2)
        )

    def angle_between(self, other: Vector) -> int:
        doc_product = self.x * other.x + self.y * other.y
        cos_a = doc_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        angle = math.atan2(self.x, self.y)
        return abs(round(math.degrees(angle)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return self.__class__(new_x, new_y)
