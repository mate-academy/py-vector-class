from __future__ import annotations
from math import sqrt, acos, degrees, cos, sin, radians


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(
            x_coord=self.x + vector.x,
            y_coord=self.y + vector.y
        )

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(
            x_coord=self.x - vector.x,
            y_coord=self.y - vector.y
        )

    def __mul__(self, vector: Vector | int | float) -> Vector:
        if isinstance(vector, Vector):
            dot_product = (self.x * vector.x) + (self.y * vector.y)
            return dot_product
        return Vector(
            x_coord=self.x * vector,
            y_coord=self.y * vector
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        vector_length = sqrt((self.x ** 2) + (self.y ** 2))
        return vector_length

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            x_coord=self.x / length,
            y_coord=self.y / length
        )

    def dot_product(self, vector: Vector) -> float:
        return round(self.x * vector.x + self.y * vector.y, 4)

    def angle_between(self, vector: Vector) -> Vector:
        dot = self.dot_product(vector)
        length_self = self.get_length()
        length_vector = vector.get_length()
        cos_a = dot / (length_self * length_vector)
        angle_rad = acos(max(-1, min(1, cos_a)))
        return round(degrees(angle_rad))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radian = radians(degrees)
        a_cos = cos(radian)
        a_sin = sin(radian)
        new_x = self.x * a_cos - self.y * a_sin
        new_y = self.x * a_sin + self.y * a_cos
        return Vector(new_x, new_y)
