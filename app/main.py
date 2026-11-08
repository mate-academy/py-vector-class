import math
from typing import Union


class Vector:
    def __init__(self, _x: int, _y: int) -> None:
        self.x = round(_x, 2)
        self.y = round(_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float]) -> \
            (Union)["Vector", int, float]:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        return round(math.degrees(math.acos(self.__mul__(other)
                     / (abs(self.get_length()) * abs(other.get_length())))), 0)

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, angle: float) -> "Vector":
        angle = math.radians(angle)
        return Vector(self.x * math.cos(angle) - self.y * math.sin(angle),
                      self.x * math.sin(angle) + self.y * math.cos(angle))
