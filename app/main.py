import math
from typing import Union, Tuple


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.x = round(end_x, 2)
        self.y = round(end_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float]) -> (
            Union)[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operation")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: Tuple[float, float],
            end_point: Tuple[float, float]) -> "Vector":
        end_x = round(end_point[0] - start_point[0], 2)
        end_y = round(end_point[1] - start_point[1], 2)
        return cls(end_x, end_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cos_a = dot_product / (len_self * len_other)
        cos_a = max(-1, min(1, cos_a))
        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)

        if angle_deg < 0:
            angle_deg += 360

        return round(min(angle_deg, 360 - angle_deg))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
