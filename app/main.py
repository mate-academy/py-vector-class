from typing import Union, Any
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other) -> "Vector":
        if isinstance(other, Vector):
            return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Any) -> Union['Vector', float, Any]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, (int, Vector)):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        vector_x = round(end_x - start_x, 2)
        vector_y = round(end_y - start_y, 2)
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        vector1_length = self.get_length()
        vector2_length = other.get_length()

        if vector1_length == 0 or vector2_length == 0:
            return 0

        cos_a = (self.x * other.x + self.y * other.y) / (vector1_length * vector2_length)

        cos_a = max(-1.0, min(1.0, cos_a))

        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self):
        positive_y_axis = Vector(0, 1)

        vector_length = self.get_length()
        y_axis_length = positive_y_axis.get_length()

        if vector_length == 0:
            return 0

        dot_product = self.x * positive_y_axis.x + self.y * positive_y_axis.y
        cos_a = dot_product / (vector_length * y_axis_length)

        cos_a = max(-1.0, min(1.0, cos_a))

        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(round(new_x, 2), round(new_y, 2))

