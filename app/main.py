import math
from math import sqrt


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: any) -> any:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: any) -> any:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: any) -> any:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> any:
        res = cls(end_point[0] - start_point[0], end_point[1] - start_point[1])
        return res

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> any:
        length = sqrt(self.x ** 2 + self.y ** 2)
        return Vector(self.x / length, self.y / length)

    def rotate(self, other: any) -> any:
        degree_to_rad = math.radians(other)
        return Vector(
            math.cos(degree_to_rad) * self.x
            - math.sin(degree_to_rad) * self.y,
            math.sin(degree_to_rad) * self.x
            + math.cos(degree_to_rad) * self.y)

    def angle_between(self, other: any) -> int:
        cos_a = (self.x * other.x + self.y * other.y) /\
                (sqrt(self.x ** 2 + self.y ** 2)
                 * sqrt(other.x ** 2 + other.y ** 2))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / sqrt(self.x ** 2 + self.y ** 2)
        return round(math.degrees(math.acos(cos_a)))
