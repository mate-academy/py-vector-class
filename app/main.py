import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(round((self.x + other.x), 2),
                      round((self.y + other.y), 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(round((self.x - other.x), 2),
                      round((self.y - other.y), 2))

    def __mul__(self, other: Union[float, int, "Vector"])\
            -> Union["Vector", float]:
        if isinstance(other, (float, int)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(round((end_point[0] - start_point[0]), 2),
                   round((end_point[1] - start_point[1]), 2))

    def get_length(self) -> float:
        return round((math.sqrt(self.x ** 2 + self.y ** 2)), 15)

    def get_normalized(self) -> "Vector":
        return Vector(round(self.x / Vector.get_length(self), 2),
                      round(self.y / Vector.get_length(self), 2))

    def angle_between(self, vector: "Vector") -> int:
        cos_a = (Vector.__mul__(self, vector)
                 / (Vector.get_length(self) * Vector.get_length(vector)))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_b = ((self.y ** 2 + Vector.get_length(self) ** 2
                  - self.x ** 2)
                 / (2 * self.y * Vector.get_length(self)))
        return round(math.degrees(math.acos(cos_b)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_new = round((self.x * math.cos(radians)
                       - self.y * math.sin(radians)), 2)
        y_new = round((self.x * math.sin(radians)
                       + self.y * math.cos(radians)), 2)
        return Vector(x_new, y_new)

    pass
