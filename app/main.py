# flake8: noqa: VNE001

from typing import Union
import math


class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"]) \
            -> Union[int, float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> Union[int, float]:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        cos_angle = (((self.x * other.x)
                      + (self.y * other.y))
                     / (((self.x ** 2 + self.y ** 2) ** 0.5)
                        * ((other.x ** 2) + (other.y ** 2)) ** 0.5))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        atan_angle = math.atan2(self.x, self.y)
        return abs(round(math.degrees(atan_angle)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
