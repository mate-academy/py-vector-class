from typing import Union, Any
import math


class Vector:
    vector_list = []

    def __init__(self, coordanate_x: float, coordanate_y: float) -> None:
        self.x = round(coordanate_x, 2)
        self.y = round(coordanate_y, 2)
        Vector.vector_list.append(self)

    @classmethod
    def is_vector(cls, other: Any) -> bool:
        return isinstance(other, Vector)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"]) -> (
            Union)[float, "Vector"]:
        if self.is_vector(other):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple, end_point: tuple)\
            -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        cos_angle = (self.__mul__(other)
                     / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_angle)), 0)

    def get_angle(self) -> float:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, angle: int) -> "Vector":
        angel_degrees = math.radians(angle)
        return Vector(self.x * math.cos(angel_degrees)
                      - self.y * math.sin(angel_degrees),
                      self.x * math.sin(angel_degrees)
                      + self.y * math.cos(angel_degrees))
