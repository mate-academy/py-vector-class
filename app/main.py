import math
from typing import Any


class Vector:
    def __init__(self, xcoord: int | float, ycoord: int | float) -> None:
        self.x = round(xcoord, 2)
        self.y = round(ycoord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other , self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(math.pow(self.x, 2)
                         + math.pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        return round(
            math.degrees(
                math.acos((self.x * other.x
                           + self.y * other.y)
                          / (self.get_length() * other.get_length()))))

    def get_angle(self) -> float:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degree: int | float) -> "Vector":
        degree = math.radians(degree)
        return Vector(
            (self.x * math.cos(degree) - self.y * math.sin(degree)),
            self.y * math.cos(degree) + self.x * math.sin(degree))
