import math
from typing import Union


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        start_x, start_y, *_ = start_point
        end_x, end_y, *_ = end_point
        return Vector(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        norm = math.sqrt(self.x**2 + self.y**2)
        if norm == 0:
            return Vector(0, 0)
        return Vector(self.x / norm, self.y / norm)

    def angle_between(self, other: "Vector") -> int:
        """
        cos(θ) = (A ⋅ B) / (∣A∣ ∣B∣)
        """
        dot_sum = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        angle_cos = dot_sum / (len_self * len_other)
        angle_rad = math.acos(max(-1.0, min(1.0, angle_cos)))
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        return self.angle_between(other=Vector(0, 2))

    def rotate(self, degrees: float) -> "Vector":
        """
        x′ = x ⋅ cos(θ) − y ⋅ sin(θ)
        y′ = x ⋅ sin(θ) + y ⋅ cos(θ)
        """
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(round(new_x, 2), round(new_y, 2))
