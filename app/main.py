from __future__ import annotations
import math


class Vector:
    vectors = []

    def __init__(self, x_vector: int | float = 0,
                 y_vector: int | float = 0) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)
        Vector.vectors.append(self)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), (round(self.y * other, 2)))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()
        cos_a = dot_product / (length_self * length_other)
        angle_radians = math.acos(cos_a)
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees

    def get_angle(self) -> float:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)

        return abs(round(angle_degrees))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(round(new_x, 2), round(new_y, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]
                                    ) -> "Vector":
        x_diff = end_point[0] - start_point[0]
        y_diff = end_point[1] - start_point[1]
        return cls(x_diff, y_diff)
