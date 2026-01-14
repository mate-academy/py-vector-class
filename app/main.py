from typing import Union
import math


class Vector:
    def __init__(self, first: float, second: float) -> None:
        self.x = round(first, 2)
        self.y = round(second, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, mul: Union[int, float, "Vector"]) \
            -> Union["Vector", int, float]:
        if isinstance(mul, Vector):
            return self.dot_product(mul)
        return Vector(self.x * mul, self.y * mul)

    def dot_product(self, other: "Vector") -> Union[int, float]:
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) \
            -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> Union[int, float]:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        qu = self.get_length()
        return Vector(self.x / qu, self.y / qu)

    def angle_between(self, other: "Vector") -> int:
        multi = self.dot_product(other)
        first_div = math.sqrt(self.x ** 2 + self.y ** 2)
        second_div = math.sqrt(other.x ** 2 + other.y ** 2)
        result = multi / (first_div * second_div)
        return round(math.degrees(math.acos(result)))

    def get_angle(self) -> int:
        angle_rad = math.atan2(abs(self.x), abs(self.y))
        angle_deg = math.degrees(angle_rad)
        if self.y >= 0:
            angle_from_y = angle_deg
        else:
            angle_from_y = 180 - angle_deg

        return round(angle_from_y)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
