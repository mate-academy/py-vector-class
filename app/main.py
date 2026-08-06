import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        x_coord = self.x + other.x
        y_coord = self.y + other.y
        return Vector(x_coord, y_coord)

    def __sub__(self, other: "Vector") -> "Vector":
        x_coord = self.x - other.x
        y_coord = self.y - other.y
        return Vector(x_coord, y_coord)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        x_coord = self.x * other
        y_coord = self.y * other
        return Vector(x_coord, y_coord)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        x_coord = self.x / length
        y_coord = self.y / length
        return Vector(x_coord, y_coord)

    def angle_between(self, other: "Vector") -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        angle = round(math.degrees(math.atan2(self.y, self.x))) - 90
        return angle if angle >= 0 else (angle + 360)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        x_coord = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_coord = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(x_coord, y_coord)
