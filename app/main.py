from typing import Union
import math


class Vector:
    def __init__(self, x_component: float, y_component: float) -> None:
        self.x = round(x_component, 2)
        self.y = round(y_component, 2)

    def __add__(self, other: Union[int, float, "Vector"]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(round(self.x + other, 2), round(self.y + other, 2))
        elif isinstance(other, Vector):
            return Vector(round(self.x + other.x, 2),
                          round(self.y + other.y, 2))

    def __sub__(self, other: Union[int, float, "Vector"]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(round(self.x - other, 2), round(self.y - other, 2))
        elif isinstance(other, Vector):
            return Vector(round(self.x - other.x, 2),
                          round(self.y - other.y, 2))

    def __mul__(self, other: Union[int, float, "Vector"]) \
            -> Union[int, float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start: tuple, end: tuple) -> "Vector":
        x_component = round(end[0] - start[0], 2)
        y_component = round(end[1] - start[1], 2)
        return Vector(x_component, y_component)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = dot_product / (len_self * len_other)
        cos_angle = max(-1, min(1, cos_angle))
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        return round(-angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(rotated_x, 2), round(rotated_y, 2))
