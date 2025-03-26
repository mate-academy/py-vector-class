import math
from typing import Tuple, Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union["Vector", int, float]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("Operand must be Vector or numeric type")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        length1 = self.get_length()
        length2 = other.get_length()
        if length1 == 0 or length2 == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_theta = dot_product / (length1 * length2)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
