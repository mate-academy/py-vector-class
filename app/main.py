from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, xray: float, yankee: float) -> None:
        self.x = round(xray, 2)
        self.y = round(yankee, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                self.x * other,
                self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return abs((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            self.x / length, self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()

        cos_angle = dot_product / (length_self * length_other)
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return int(round(angle_degrees))

    def get_angle(self) -> float:
        length = self.get_length()
        result = math.acos(self.y / length)
        return int(round(math.degrees(result)))

    def rotate(self, rotation: int) -> Vector:
        rad = math.radians(rotation)
        cos_theta = math.cos(rad)
        sin_theta = math.sin(rad)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
