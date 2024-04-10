import math
from typing import Union


class Vector:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector"]) -> Union["Vector", int, float]:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        x_positions = end_point[0] - start_point[0]
        y_positions = end_point[1] - start_point[1]
        return cls(x_positions, y_positions)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: object) -> float:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            module_vectors = self.get_length() * other.get_length()
            cos_a = dot_product / module_vectors
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        degree = self.y / self.get_length()
        angle_y = math.degrees(math.acos(degree))
        return round(angle_y)

    def rotate(self, degrees: int) -> object:
        angle_radians = math.radians(degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)
        x_value = self.x * cos_theta - self.y * sin_theta
        y_value = self.x * sin_theta + self.y * cos_theta
        return Vector(x_value, y_value)
