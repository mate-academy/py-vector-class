from __future__ import annotations
import math


class Vector:
    def __init__(self, new_x: float, new_y: float) -> None:
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, multiplier: Vector | float) -> Vector | float:
        if isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y
        else:
            return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        cos_a = (
            (self.x * vector.x + self.y * vector.y)
            / (self.get_length() * vector.get_length())
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        angle_y = 90 - math.degrees(math.atan2(self.y, self.x))

        if angle_y < 0:
            angle_y += 360

        if angle_y > 180:
            angle_y = 360 - angle_y

        return round(angle_y)

    def rotate(self, ange: int) -> Vector:
        angle_radians = math.radians(ange)
        return Vector(
            self.x * math.cos(angle_radians)
            - self.y * math.sin(angle_radians),
            self.x * math.sin(angle_radians)
            + self.y * math.cos(angle_radians)
        )
