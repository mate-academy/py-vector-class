import math
from typing import Union


class Vector:
    def __init__(self,
                 x_vector: Union[int, float],
                 y_vector: Union[int, float]) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: dict,
                                    end_point: dict) -> "Vector":
        x_diff = end_point[0] - start_point[0]
        y_diff = end_point[1] - start_point[1]
        return cls(x_diff, y_diff)

    def get_length(self) -> Union[int, float]:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other_vector: "Vector") -> Union[int, float]:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        length_self = self.get_length()
        length_other = other_vector.get_length()
        cos_angle = dot_product / (length_self * length_other)
        cos_angle = max(-1, min(1, cos_angle))
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> Union[int, float]:
        cos_angle = self.y / self.get_length()
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: Union[int, float]) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
