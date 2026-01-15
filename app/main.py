import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_component: float, y_component: float) -> None:
        self.x = round(x_component, 2)
        self.y = round(y_component, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float, int]
                ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        delta_x = round(end_point[0] - start_point[0], 2)
        delta_y = round(end_point[1] - start_point[1], 2)
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        cos_angle = dot_product / length_product
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        if angle_deg < 0:
            angle_deg += 360
        if angle_deg > 180:
            angle_deg = 360 - angle_deg
        return round(angle_deg)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
