import math
from typing import Any


class Vector:

    def __init__(self, coord_x: (int, float), coord_y: (int, float)) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: (int, float)) -> Any:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: (int, float)) -> Any:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (int, float)) -> Any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Any:
        coord_x = end_point[0] - start_point[0]
        coord_y = end_point[1] - start_point[1]
        return cls(coord_x, coord_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Any:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: (int, float)) -> float:
        dot_product = self * other
        cosine = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: (int, float)) -> Any:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
