from typing import Callable, Union
import math


class Vector:

    def __init__(
            self,
            dot_x: Union[int, float],
            dot_y: Union[int, float]
    ) -> None:
        self.x = round(dot_x, 2)
        self.y = round(dot_y, 2)

    def __add__(self, other: Callable) -> Callable:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Callable) -> Callable:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union[int, float, Callable]
                ) -> Callable | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Callable:
        return Vector(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self: Callable) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Callable:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Callable) -> int:
        dot_product = sum(
            x * y for x, y in zip(
                (self.x, self.y),
                (vector.x, vector.y)
            )
        )
        cosine_angle = dot_product / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cosine_angle)))

    def get_angle(self) -> int:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Callable:
        cos_theta = math.cos(math.radians(degrees))
        sin_theta = math.sin(math.radians(degrees))
        rotated_x = round(self.x * cos_theta - self.y * sin_theta, 2)
        rotated_y = round(self.x * sin_theta + self.y * cos_theta, 2)
        self.x = rotated_x
        self.y = rotated_y
        return self
