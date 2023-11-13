import math
from math import acos, degrees, sqrt, cos, sin, radians


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: int) -> int:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int) -> int:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return Vector(end_point[0]
                      - start_point[0], end_point[1]
                      - start_point[1])

    def get_length(self) -> int:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> int:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: tuple) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_product = self.get_length() * other.get_length()
        cos_angle = dot_product / magnitude_product
        angle_in_radians = acos(cos_angle)
        angle_in_degrees = round(degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> "Vector":
        angle_in_radians = radians(degrees)
        new_x = self.x * cos(angle_in_radians) - self.y * sin(angle_in_radians)
        new_y = self.x * sin(angle_in_radians) + self.y * cos(angle_in_radians)
        return Vector(new_x, new_y)
