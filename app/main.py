import math
from typing import Self, Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)

    def __add__(self, other_vector: Self) -> Self:
        return Vector(self.x + other_vector.x,
                      self.y + other_vector.y)

    def __sub__(self, other_vector: Self) -> Self:
        return Vector(self.x - other_vector.x,
                      self.y - other_vector.y)

    def __mul__(self, multiplier: Union[Self, float,
                int]) -> Union[Self, float]:
        if isinstance(multiplier, Vector):
            return (self.x * multiplier.x
                    + self.y * multiplier.y)
        return Vector(self.x * multiplier, self.y
                      * multiplier)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Self:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Self:
        vector_length = self.get_length()
        if vector_length == 0:
            return Vector(0, 0)
        return Vector(self.x / vector_length,
                      self.y / vector_length)

    def angle_between(self, other_vector: Self) -> int:
        length_one = self.get_length()
        length_two = other_vector.get_length()
        if length_one == 0 or length_two == 0:
            return 0
        dot_product = self * other_vector
        cosine_value = max(-1.0, min(1.0, dot_product / (length_one
                                                         * length_two)))
        angle_in_degrees = math.degrees(math.acos(cosine_value))
        return int(round(angle_in_degrees))

    def get_angle(self) -> int:
        angle_in_radians = math.atan2(self.x,
                                      self.y)
        angle_in_degrees = math.degrees(angle_in_radians)
        return int(round(angle_in_degrees))

    def rotate(self, rotation_degrees: int) -> Self:
        radians_angle = math.radians(rotation_degrees)
        cos_theta = math.cos(radians_angle)
        sin_theta = math.sin(radians_angle)
        new_horizontal = self.x * cos_theta
        - self.y * sin_theta
        new_vertical = self.x * sin_theta
        + self.y * cos_theta
        return Vector(new_horizontal, new_vertical)
