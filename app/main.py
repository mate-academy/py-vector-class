import math
from typing import Tuple, Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            round(self.coord_x + other.coord_x, 2),
            round(self.coord_y + other.coord_y, 2),
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            round(self.coord_x - other.coord_x, 2),
            round(self.coord_y - other.coord_y, 2),
        )

    def __mul__(self, other: Union["Vector", float, int])\
            -> Union["Vector", float]:
        if isinstance(other, Vector):
            dot_product = (
                self.coord_x * other.coord_x
                + self.coord_y * other.coord_y
            )
            return dot_product
        elif isinstance(other, (int, float)):
            return Vector(
                round(self.coord_x * other, 2),
                round(self.coord_y * other, 2),
            )
        else:
            raise TypeError("Multiplication with type not supported")

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float],
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.coord_x / length, 2),
            round(self.coord_y / length, 2),
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            return 0
        cos_angle = dot_product / (length_self * length_other)
        cos_angle = max(min(cos_angle, 1), -1)  # evitar erros de domínio
        angle_rad = math.acos(cos_angle)
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self) -> int:
        # ângulo entre vetor e eixo Y positivo
        angle_rad = math.atan2(self.coord_x, self.coord_y)
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        rotated_x = self.coord_x * cos_theta - self.coord_y * sin_theta
        rotated_y = self.coord_x * sin_theta + self.coord_y * cos_theta
        return Vector(rotated_x, rotated_y)
