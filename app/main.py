import math
from typing import Union


class Vector:

    def __init__(self, x_coord: Union[int, float],
                 y_coord: Union[int, float]) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coord + other.x_coord,
                      self.y_coord + other.y_coord)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coord - other.x_coord,
                      self.y_coord - other.y_coord)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        if isinstance(other, (int, float)):
            return Vector(self.x_coord * other, self.y_coord * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float]
                                    , end_point: tuple[float, float])\
            -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return (self.x_coord ** 2 + self.y_coord ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, vector: "Vector") -> int:
        dot = self.x_coord * vector.x_coord + self.y_coord * vector.y_coord
        lengths = self.get_length() * vector.get_length()
        cos_a = dot / lengths
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        dot = self.y_coord
        lengths = self.get_length()  # |(0,1)| = 1
        cos_a = dot / lengths
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x_coord * cos_a - self.y_coord * sin_a
        new_y = self.x_coord * sin_a + self.y_coord * cos_a
        return Vector(new_x, new_y)
