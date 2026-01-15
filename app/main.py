import math
from typing import Union


class Vector:
    def __init__(self, x1: int | float, y1: int | float) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: callable) -> callable:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y)

    def __mul__(self, other: Union[int, "Vector"]) -> Union[int, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: "Vector") -> int:
        angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 100))

    def rotate(self, degrees: int) -> callable:
        rd = math.radians(degrees)
        new_x = (self.x * math.cos(rd) - self.y * math.sin(rd))
        new_y = (self.x * math.sin(rd) + self.y * math.cos(rd))

        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> callable:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )
