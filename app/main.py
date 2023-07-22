from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            variable_x: int | float,
            variable_y: int | float
    ) -> None:
        self.x = round(variable_x, 2)
        self.y = round(variable_y, 2)

    def __add__(self, another: Vector) -> Vector:
        return Vector(self.x + another.x, self.y + another.y)

    def __sub__(self, another: Vector) -> Vector:
        return Vector(self.x - another.x, self.y - another.y)

    def __mul__(self, element: int | float | Vector) -> Vector | int | float:
        if isinstance(element, (int, float)):
            return Vector(self.x * element, self.y * element)

        return (self.x * element.x) + (self.y * element.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector((self.x / length), self.y / length)

    def angle_between(self, another: Vector) -> int | float:
        return round(
            math.degrees(
                math.acos((self.__mul__(another))
                          / (self.get_length() * another.get_length())))
        )

    def get_angle(self) -> int | float:
        another = Vector(0, 1)
        return round(
            math.degrees(
                math.acos((self.__mul__(another))
                          / (self.get_length() * another.get_length())))
        )

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            (math.cos(degrees) * self.x) - (math.sin(degrees) * self.y),
            (math.sin(degrees) * self.x) + (math.cos(degrees) * self.y)
        )
