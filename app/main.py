import math
from typing import Any


class Vector:

    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: int) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> Any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int , float)):
            return Vector(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> Any:
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: int,
                                    end_point: int) -> "Vector":
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int) -> float:
        dot = self * other
        lengths = (self.get_length() * other.get_length())
        if lengths == 0:
            return 0
        cos_theta = dot / lengths
        cos_theta = max(-1 , min(1, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.x, self.y))
        return round(abs(angle))

    def rotate(self, angle: float) -> "Vector":
        rad = math.radians(angle)
        x_angle = math.cos(rad) * self.x - math.sin(rad) * self.y
        y_angle = math.sin(rad) * self.x + math.cos(rad) * self.y
        return Vector(x_angle, y_angle)
