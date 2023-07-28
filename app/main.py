import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        add_x = self.x + other.x
        add_y = self.y + other.y
        return Vector(add_x, add_y)

    def __sub__(self, other: "Vector") -> "Vector":
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            mul_x = round(self.x * other, 2)
            mul_y = round(self.y * other, 2)
            return Vector(mul_x, mul_y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_radians = math.acos(cos_angle)    # we use it to get the inverse function for the cosine
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        angle_int = int(round(angle_deg))
        return angle_int

    def rotate(self, degrees: int) -> "Vector":
        angle_radians = math.radians(degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)
        f_new_x = cos_theta * self.x - sin_theta * self.y
        f_new_y = sin_theta * self.x + cos_theta * self.y
        return Vector(f_new_x, f_new_y)
