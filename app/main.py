from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    @property
    def x(self) -> Vector:
        return self.coord_x

    @property
    def y(self) -> Vector:
        return self.coord_y

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.coord_x + other.coord_x,
                          self.coord_y + other.coord_y)
        raise TypeError(f"Unsupported type for addition: {type(other)}")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.coord_x - other.coord_x,
                          self.coord_y - other.coord_y)
        raise TypeError(f"Unsupported type for subtraction: {type(other)}")

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            dot_product = ((self.coord_x * other.coord_x)
                           + (self.coord_y * other.coord_y))
            return dot_product
        elif isinstance(other, (int, float)):
            return Vector(self.coord_x * other, self.coord_y * other)
        raise TypeError(f"Unsupported type for subtraction: {type(other)}")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) \
            -> Vector:
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return Vector(coord_x, coord_y)

    def get_length(self) -> int | float:
        vector_length = math.sqrt((self.coord_x * self.coord_x)
                                  + (self.coord_y * self.coord_y))
        return vector_length

    def get_normalized(self) -> Vector:
        vector_lenght = self.get_length()
        return Vector(self.coord_x / vector_lenght,
                      self.coord_y / vector_lenght)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_product = self.__mul__(other)
            lengths_product = self.get_length() * other.get_length()
            if lengths_product == 0:
                raise ValueError("Один из векторов нулевой")
            else:
                cos_theta = round(math.degrees(math.acos(dot_product
                                                         / lengths_product)))
            return cos_theta

    def get_angle(self) -> int | float:
        if self.get_length() == 0:
            return 0
        cos_theta = round(math.degrees(math.acos(self.coord_y
                                                 / self.get_length())))
        return cos_theta

    def rotate(self, degrees: int) -> Vector:
        radians_degres = math.radians(degrees)
        new_x = ((self.coord_x * math.cos(radians_degres))
                 - (self.coord_y * math.sin(radians_degres)))
        new_y = ((self.coord_x * math.sin(radians_degres))
                 + (self.coord_y * math.cos(radians_degres)))
        return Vector(new_x, new_y)
