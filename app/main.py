from __future__ import annotations
from typing import Union, Any
import math


class Vector:

    def __init__(self,
                 x_cord: Union[float, int],
                 y_cord: Union[float, int]
                 ) -> None:
        if (not isinstance(x_cord, (float, int))
                or not isinstance(y_cord, (float, int))):
            raise TypeError(
                f"Vector expecting only int or float, got:\n"
                f"""{'' if isinstance(x_cord, (float, int)) else
                '>>> x - ' + type(x_cord).__name__}"""
                f"""{'' if isinstance(y_cord, (float, int)) else
                '>>> y - ' + type(y_cord).__name__}"""
            )
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    @staticmethod
    def check_other(other: Any) -> Vector:
        if isinstance(other, Vector):
            return other

        if not isinstance(other, (float, int)):
            raise TypeError(
                f">>> supported operand type(s) "
                f"for mathematical operations is only: float, int\n"
                f"got: {type(other).__name__}"
            )
        return Vector(other, other)

    def __add__(self,
                other: Union[Vector, float, int]
                ) -> Vector:
        other = self.check_other(other)
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self,
                other: Union[Vector, float, int]
                ) -> Vector:
        other = self.check_other(other)
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union[Vector, float, int]
                ) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(
                f">>> supported operand type(s) "
                f"for mathematical operations is only: float, int\n"
                f"got: {type(other).__name__}"
            )

    @staticmethod
    def create_vector_by_two_points(start_point: list,
                                    end_point: list
                                    ) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:

        length = self.get_length()
        if length == 0:
            raise ValueError(
                ">>> cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        other = self.check_other(other)
        self_length = self.get_length()
        other_length = other.get_length()

        if self_length == 0 or other_length == 0:
            raise ValueError(
                ">>> Cannot compute angle with zero-length vector")
        cos_theta = (self * other) / (self_length * other_length)
        cos_theta = max(min(cos_theta, 1), -1)

        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError(
                ">>> Cannot compute angle with zero-length vector")

        cos_theta = self.y / length
        cos_theta = max(min(cos_theta, 1), -1)

        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
