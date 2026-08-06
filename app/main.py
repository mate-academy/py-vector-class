import math
from typing import Any


class Vector:
    def __init__(self, x: [int, float], y: [int, float]) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: [int, float]) -> "Vector":
        x = round(self.x + other.x, 2)
        y = round(self.y + other.y, 2)
        return Vector(x, y)

    def __sub__(self, other: [int, float]) -> "Vector":
        x = round(self.x - other.x, 2)
        y = round(self.y - other.y, 2)
        return Vector(x, y)

    def __mul__(self, other: [int, float]) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            x = round(self.x * other, 2)
            y = round(self.y * other, 2)
            return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> Any:
        vector_len = math.sqrt(self.x ** 2 + self.y ** 2)
        return vector_len

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: [int, float]) -> int:
        numerator = self.x * other.x + self.y * other.y
        denominator = \
            (math.sqrt(self.x ** 2 + self.y ** 2) * \
             (math.sqrt(other.x ** 2 + other.y ** 2)))
        cos_a = numerator / denominator
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def get_angle(self) -> int:
        cos_a = self.y / (math.sqrt(self.x ** 2 + self.y ** 2))
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def rotate(self, degrees: int) -> "Vector":
        convert_to_radians = math.radians(degrees)
        cs = math.cos(convert_to_radians)
        sn = math.sin(convert_to_radians)
        x = self.x * cs - self.y * sn
        y = self.x * sn + self.y * cs
        return Vector(x, y)
