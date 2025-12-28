from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, vector_2: Vector) -> Vector:
        add_x = self.x + vector_2.x
        add_y = self.y + vector_2.y
        return Vector(add_x, add_y)

    def __sub__(self, vector_2: Vector) -> Vector:
        sub_x = self.x - vector_2.x
        sub_y = self.y - vector_2.y
        return Vector(sub_x, sub_y)

    def __mul__(self, vector_2: Vector | int | float) -> Vector | int | float:
        if isinstance(vector_2, int | float):
            mul_x = self.x * vector_2
            mul_y = self.y * vector_2
            return Vector(mul_x, mul_y)
        else:
            return self.x * vector_2.x + self.y * vector_2.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return cls(coord_x, coord_y)

    def get_length(self) -> float:
        return abs(math.sqrt(self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector_2: Vector) -> int:
        cos_a = ((self.__mul__(vector_2))
                 / (self.get_length() * vector_2.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, angle: int) -> Vector:
        radians = math.radians(angle)
        coord_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        coord_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(coord_x, coord_y)
