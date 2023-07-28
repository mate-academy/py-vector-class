import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]
                                    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

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
        angle_radians = math.acos(cos_angle)
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
        new_x = cos_theta * self.x - sin_theta * self.y
        new_y = sin_theta * self.x + cos_theta * self.y
        return Vector(new_x, new_y)
