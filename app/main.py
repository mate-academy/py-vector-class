import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union[int, float, "Vector"]
    ) -> Union[float, "Vector"]:
        pass

        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[float, float],
            end_point: Tuple[float, float]
    ) -> "Vector":
        pass

        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        angle_rad = math.acos(dot_product / lengths_product)
        angle = math.degrees(angle_rad)
        return round(angle) if round(angle) <= 180 else 360 - round(angle)

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: float) -> "Vector":
        angle_rad = math.radians(degrees)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(new_x, new_y)
