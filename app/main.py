from __future__ import annotations
import math


class Vector:
    def __init__(self, vec_x: float, vec_y: float) -> None:
        self.x = round(vec_x, 2)
        self.y = round(vec_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = round(self.x + other.x, 2)
        new_y = round(self.y + other.y, 2)
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = round(self.x - other.x, 2)
        new_y = round(self.y - other.y, 2)
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        new_x = round(end_point[0] - start_point[0], 2)
        new_y = round(end_point[1] - start_point[1], 2)
        return Vector(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            new_x = round(self.x / length, 2)
            new_y = round(self.y / length, 2)
            return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> float | None:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            return None
        else:
            cos_theta = dot_product / magnitude_product
            return math.ceil(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)
        if angle_deg < 0:
            angle_deg += 360

        return round(angle_deg) - 90

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)
        new_x = round(self.x * math.cos(angle_rad)
                      - self.y * math.sin(angle_rad), 2)
        new_y = round(self.x * math.sin(angle_rad)
                      + self.y * math.cos(angle_rad), 2)
        return Vector(new_x, new_y)
