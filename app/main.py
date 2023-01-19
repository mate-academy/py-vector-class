from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            vector = Vector(
                point_x=(self.x + other.x),
                point_y=(self.y + other.y)
            )
        return vector

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            vector = Vector(
                point_x=(self.x - other.x),
                point_y=(self.y - other.y)
            )
        return vector

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = ((self.x * other.x)
                           + (self.y * other.y))
            return dot_product
        vector = Vector(
            point_x=(self.x * other),
            point_y=(self.y * other))
        return vector

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            point_x=(end_point[0] - start_point[0]),
            point_y=(end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            point_x=round(self.x / Vector.get_length(self), 2),
            point_y=round(self.y / Vector.get_length(self), 2)
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self.__mul__(other)) / (self.get_length()
                                         * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y
                                            / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        rotated_vector = Vector(
            point_x=self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            point_y=self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
        return rotated_vector
