from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y

        return Vector(new_x, new_y)

    def __mul__(self, num: float | Vector) -> Vector:
        if isinstance(num, (int, float)):
            return Vector(self.x * num, self.y * num)
        elif isinstance(num, Vector):
            return self.x * num.x + self.y * num.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]

        return cls(point_x, point_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()

        normalized_x = self.x / length
        normalized_y = self.y / length

        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        product = self.x * other.x + self.y * other.y

        magnitude_self = self.get_length()
        magnitude_other = other.get_length()

        cos_a = product / (magnitude_self * magnitude_other)

        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def get_angle(self) -> int:
        magnitude_self = self.get_length()

        cos_a = self.y / magnitude_self

        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
