from typing import Union
import math


class Vector:

    @classmethod
    def create_vector_by_two_points(
            cls, start_vector: tuple, end_vector: tuple) -> "Vector":
        return cls(
            end_vector[0] - start_vector[0], end_vector[1] - start_vector[1]
        )

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"]) \
            -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return self.__class__(self.x * other, self.y * other)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(
            self.x / self.get_length(), self.y / self.get_length()
        )

    def get_angle(self) -> int:
        if self.y < 0:
            return 180 - round(
                math.degrees(math.asin(abs(self.x) / self.get_length())), 0
            )

        return round(
            math.degrees(math.asin(abs(self.x) / self.get_length())), 0
        )

    def angle_between(self, other: "Vector") -> int:
        if isinstance(other, Vector):
            angle_self = self.get_angle()
            angle_other = other.get_angle()
            if self.x < 0:
                angle_self = 360 - angle_self
            if other.x < 0:
                angle_other = 360 - angle_other
            return abs(angle_self - angle_other)

    def rotate(self, angle: int) -> "Vector":
        old_angle = self.get_angle()
        if self.y < 0:
            old_angle *= -1
        new_angle = old_angle - angle
        if new_angle < 0:
            new_angle = new_angle % -360
        else:
            new_angle = new_angle % 360
        return Vector(
            math.sin(math.radians(new_angle)) * self.get_length(),
            math.cos(math.radians(new_angle)) * self.get_length()
        )
