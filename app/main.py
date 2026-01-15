from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=round(self.x / self.get_length(), 2),
            y_coord=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()

        if magnitude_product == 0:
            return 0

        cos_angle = dot_product / magnitude_product
        angle_in_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        if self.x == 0:
            return 0
        angle_radians = math.atan2(self.y, self.x)
        angle_degrees = math.degrees(angle_radians)
        result = round((angle_degrees + 360) % 360)

        if self.x < 0:
            result -= 90

        return result

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
