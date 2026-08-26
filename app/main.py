import math
from typing import Union, Tuple


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.point_x = round(point_x, 2)
        self.point_y = round(point_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.point_x + other.point_x, self.point_y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.point_x - other.point_x, self.point_y - other.point_y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(round(self.point_x * other, 2), round(self.point_y * other, 2))
        elif isinstance(other, Vector):
            dot_product = self.point_x * other.point_x + self.point_y * other.point_y
            return dot_product
        else:
            raise TypeError("Multiplication with unsupported type")

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) -> "Vector":
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return cls(point_x, point_y)

    def get_length(self) -> float:
        return math.sqrt(self.point_x ** 2 + self.point_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.point_x / length, self.point_y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_theta = dot_product / length_product
        cos_theta = max(min(cos_theta, 1), -1)
        angle_radians = math.acos(cos_theta)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.point_x * math.cos(radians) - self.point_y * math.sin(radians)
        new_y = self.point_x * math.sin(radians) + self.point_y * math.cos(radians)
        return Vector(new_x, new_y)
