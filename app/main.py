import math
from typing import Union


class Vector:
    def __init__(self, x1: float, y1: float) -> None:
        self.x1 = round(x1, 2)
        self.y1 = round(y1, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x1 + other.x1, self.y1 + other.y1)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x1 - other.x1, self.y1 - other.y1)
        return NotImplemented

    def __mul__(self, other: Union["Vector", float, int]) \
            -> Union["Vector", float]:
        if isinstance(other, (int, float)):  # Умножение вектора на число
            return Vector(self.x1 * other, self.y1 * other)
        elif isinstance(other, Vector):  # Скалярное произведение двух векторов
            return self.x1 * other.x1 + self.y1 * other.y1
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        if (isinstance(start_point, tuple) and len(start_point) == 2
                and isinstance(end_point, tuple) and len(end_point) == 2):
            return cls(
                end_point[0] - start_point[0], end_point[1] - start_point[1]
            )
        return NotImplemented

    def det_length(self) -> float:
        return math.sqrt(self.x1 ** 2 + self.y1 ** 2)

    def get_normalized(self) -> "Vector":
        length = self.det_length()
        return Vector(self.x1 / length, self.y1 / length)

    def angle_between(self, vector: "Vector") -> int:
        dot_prod = self.x1 * vector.x1 + self.y1 * vector.y1
        length_self = self.det_length()
        length_vector = vector.det_length()
        cos_a = dot_prod / (length_self * length_vector)
        cos_a = max(min(cos_a, 1.0), -1.0)
        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        length = self.det_length()
        cos_a = self.y1 / length
        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x1 * cos_theta - self.y1 * sin_theta
        new_y = self.x1 * sin_theta + self.y1 * cos_theta
        return Vector(new_x, new_y)
