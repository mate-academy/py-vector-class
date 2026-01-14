import math
from typing import Union


class Vector:

    def __init__(self, x_vect: int, y_vect: int) -> None:
        self.x = round(x_vect, 2)
        self.y = round(y_vect, 2)

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"]
                ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        mag = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(self.x / mag, self.y / mag)

    def angle_between(self, other: "Vector") -> int:
        scalar_vector = self * other
        length_one = self.get_length()
        length_too = other.get_length()
        return round(math.degrees
                     (math.acos(scalar_vector / (length_one * length_too))))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return abs(round(angle_deg))

    def rotate(self, degrees: int) -> "Vector":
        angle_rad = math.radians(degrees)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(new_x, new_y)
