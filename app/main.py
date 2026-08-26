from __future__ import annotations
import math


class Vector:
    def __init__(self,
                 x_value: int | float,
                 y_value: int | float) -> None:
        self.x = round(x_value,
                       2)
        self.y = round(y_value,
                       2)

    def __str__(self) -> str:
        return f"Vector (x={self.x}, y={self.y})"

    def __add__(self,
                other: Vector) -> Vector:
        return Vector(x_value=self.x + other.x,
                      y_value=self.y + other.y)

    def __sub__(self,
                other: Vector) -> Vector:
        return Vector(x_value=self.x - other.x,
                      y_value=self.y - other.y)

    def __mul__(self,
                other: int | float | Vector) -> Vector | int | float:
        if isinstance(other,
                      Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_value=self.x * other,
                      y_value=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_value=end_point[0] - start_point[0],
            y_value=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_value=self.x / self.get_length(),
            y_value=self.y / self.get_length()
        )

    def angle_between(self,
                      other: Vector) -> int:
        cos_angle = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        y_axis = Vector(x_value=0,
                        y_value=1)
        cos_angle = self * y_axis / (self.get_length() * y_axis.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self,
               degrees: int) -> Vector:
        rad_degree = math.radians(degrees)
        x_value = self.x * math.cos(rad_degree) - self.y * math.sin(rad_degree)
        y_value = self.x * math.sin(rad_degree) + self.y * math.cos(rad_degree)
        return Vector(x_value=x_value,
                      y_value=y_value)
