from math import sqrt, degrees, acos, radians, cos, sin
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None: # noqa VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(
            self,
            other: Union["Vector", float]
    ) -> Union["Vector", float, None]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def dot_product(self, other: "Vector") -> float:
        return round(self.x * other.x + self.y * other.y, 4)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1]
                      )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        if length == 0:
            return Vector(self.x, self.y)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        cos_a = (self.dot_product(other)
                 / (self.get_length() * other.get_length()))
        cos_a = max(-1, min(1, cos_a))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> float:
        other = Vector(0, 1)
        cos_a = (self.dot_product(other)
                 / (self.get_length() * other.get_length()))
        return round(degrees(acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        alfa = radians(degrees)
        x1 = self.x * cos(alfa) - self.y * sin(alfa)
        y1 = self.x * sin(alfa) + self.y * cos(alfa)
        return Vector(x1, y1)
