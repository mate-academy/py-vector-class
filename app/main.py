import math
from typing import Self, Union


class Vector:
    def __init__(self, x: float, y: float) -> None:        
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Self, float, int]) -> Union[Self, float]:
        if isinstance(other, Vector):            
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float], end_point: tuple[float, float]) -> Self:
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Self:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Self) -> int:
        len1 = self.get_length()
        len2 = other.get_length()
        if len1 == 0 or len2 == 0:
            return 0

        dot = self * other
        cos_theta = max(-1.0, min(1.0, dot / (len1 * len2)))
        return int(round(math.degrees(math.acos(cos_theta))))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def rotate(self, degrees: int) -> Self:
        rad = math.radians(degrees)
        cos_r = math.cos(rad)
        sin_r = math.sin(rad)
        new_x = self.x * cos_r - self.y * sin_r
        new_y = self.x * sin_r + self.y * cos_r
        return Vector(new_x, new_y)
