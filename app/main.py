from collections.abc import Callable
import math


class Vector:
    def __init__(self, xx: float | int, yy: float | int) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Callable) -> Callable:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Callable) -> Callable:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Callable | float | int) -> Callable | float :
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Callable:
        sx, sy = start_point
        ex, ey = end_point
        return cls(ex - sx, ey - sy)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Callable:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Callable) -> int:
        cos = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        axis_y = Vector(0, 1)
        return self.angle_between(axis_y)

    def rotate(self, degrees: int) -> Callable:
        radians = math.radians(degrees)
        rot_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rot_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(rot_x, rot_y)
