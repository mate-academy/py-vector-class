from __future__ import annotations
import math


class Vector:
    def __init__(self, x_var: float | int, y_var: float | int) -> None:
        self.x_var = round(x_var, 2)
        self.y_var = round(y_var, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_var=self.x_var + other.x_var,
                      y_var=self.y_var + other.y_var)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_var=self.x_var - other.x_var,
                      y_var=self.y_var - other.y_var)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x_var * other.x_var) + (self.y_var * other.y_var)
        return Vector(x_var=other * self.x_var,
                      y_var=other * self.y_var)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(x_var=list(end_point)[0] - list(start_point)[0],
                   y_var=list(end_point)[1] - list(start_point)[1])

    def get_length(self) -> float | int:
        return (self.x_var ** 2 + self.y_var ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        initial_length = self.get_length()
        normalized_x = self.x_var / initial_length
        normalized_y = self.y_var / initial_length
        return Vector(x_var=normalized_x,
                      y_var=normalized_y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        product_of_magnitudes = (self.get_length()
                                 * other.get_length())
        value_of_arccosine = math.acos(dot_product
                                       / product_of_magnitudes)
        angle = round(math.degrees(value_of_arccosine))
        return angle

    def get_angle(self) -> int:
        radian_angle_to_y_axis = math.atan2(self.x_var, self.y_var)
        degrees_angle_to_y_axis = abs(math.degrees(radian_angle_to_y_axis))
        return round(degrees_angle_to_y_axis)

    def rotate(self, degrees: int) -> Vector:
        degrees_to_radians = math.radians(degrees)
        sinus_value = math.sin(degrees_to_radians)
        cosine_value = math.cos(degrees_to_radians)
        new_x = cosine_value * self.x_var - sinus_value * self.y_var
        new_y = sinus_value * self.x_var + cosine_value * self.y_var
        return Vector(x_var=new_x, y_var=new_y)

    pass
