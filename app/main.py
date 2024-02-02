from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int | float):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        return Vector(
            x=self.x / len_vector,
            y=self.y / len_vector
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        cosine_theta = dot_product / length_product

        angle_in_degrees = round(math.degrees(math.acos(cosine_theta)))

        return angle_in_degrees

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)

        angle_deg = ((angle_deg + 270) % 360)
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        new_x = round(new_x, 2)
        new_y = round(new_y, 2)

        return Vector(new_x, new_y)
