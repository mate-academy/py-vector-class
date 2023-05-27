import math
from typing import Union


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Union["Vector", float, int])\
            -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float],
                                    end_point: tuple[float]) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: "Vector") -> float | int:
        return round(math.degrees
                     (math.acos((self * other)
                                / (self.get_length() * other.get_length()))))
        # θ = arccos((a · b) / (|a| * |b|))

    def get_angle(self) -> float | int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        x_rotated = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_rotated = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(x_rotated, y_rotated)
