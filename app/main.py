from typing import Union
import math


class Vector:
    def __init__(self, abscissa: float, ordinate: float) -> None:
        self.x = round(abscissa, 2)
        self.y = round(ordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        new_x = self.x * other
        new_y = self.y * other
        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        new_x = self.x / length
        new_y = self.y / length
        return Vector(new_x, new_y)

    def angle_between(self, other: "Vector") -> int:
        numerator = self.x * other.x + self.y * other.y
        denominator = self.get_length() * other.get_length()
        radian_angle = math.acos(numerator / denominator)
        return round(radian_angle * 180 / math.pi)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 5))

    def rotate(self, degrees: int) -> "Vector":
        degrees = math.radians(degrees)
        new_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        new_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(new_x, new_y)
