import math
from typing import Self, Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)

    def __add__(self, other_vector: Self) -> Self:
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: Self) -> Self:
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self,
                multiplier: Union[Self, float, int]) -> Union[Self, float]:
        if isinstance(multiplier, Vector):
            return (self.x * multiplier.x) + (self.y * multiplier.y)
        return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> Self:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Self:
        vector_length = self.get_length()
        if vector_length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other_vector: Self) -> int:
        len_one = self.get_length()
        len_two = other_vector.get_length()
        if len_one == 0 or len_two == 0:
            return 0
        dot_product = self * other_vector
        cos_val = max(-1.0, min(1.0, dot_product / (len_one * len_two)))
        return int(round(math.degrees(math.acos(cos_val))))

    def get_angle(self) -> int:
        angle_degrees = math.degrees(math.atan2(self.x, self.y))
        return int(round(angle_degrees % 360))

    def rotate(self, rotation_degrees: int) -> Self:
        rad_val = math.radians(rotation_degrees)
        cos_val = math.cos(rad_val)
        sin_val = math.sin(rad_val)
        new_x = (self.x * cos_val) - (self.y * sin_val)
        new_y = (self.x * sin_val) + (self.y * cos_val)
        return Vector(new_x, new_y)
