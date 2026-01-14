from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length(),
        )

    def angle_between(self, vector: Vector) -> int:
        dot_product = self * vector
        self_length = self.get_length()
        other_length = vector.get_length()
        if self_length == 0 or other_length == 0:
            return 0  # Return 0 if any of the vectors has zero length

        # Ensure the value passed to math.acos() falls within the valid range
        cos_angle = min(1, max(-1, dot_product / (self_length * other_length)))
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        return abs(
            round(
                math.degrees(
                    math.atan2(self.x, self.y)
                )
            )
        )

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
