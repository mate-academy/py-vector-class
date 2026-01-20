import math
from typing import Union, Tuple


class Vector:
    def __init__(self, p_x: float, p_y: float) -> None:
        self.x = round(p_x, 2)
        self.y = round(p_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x, self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x, self.y - other.y
        )

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2), round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            dot_product = (
                self.x * other.x + self.y * other.y
            )
            return dot_product
        else:
            raise TypeError("Multiplication with unsupported type")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

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
        new_x = (
            self.x * math.cos(radians) - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
        return Vector(new_x, new_y)
