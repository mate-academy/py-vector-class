import math
from typing import Union


class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]
                 ) -> Union[int, float]:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Union[int, float]) -> Union[int, float]:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Union[int, float]) -> Union[int, float]:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float]) -> Union[int, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    def get_length(self) -> Union[int, float]:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 15)

    def get_normalized(self) -> Union[int, float]:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Union[int, float]) -> Union[int, float]:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> Union[int, float]:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: Union[int, float]) -> Union[int, float]:
        radians = math.radians(degrees)
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: Union[int, float],
                                    end_point: Union[int, float]
                                    ) -> Union[int, float]:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)
