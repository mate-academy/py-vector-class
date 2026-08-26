from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: int | float, point_y: int | float) -> None:

        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                point_x=self.x + other.x,
                point_y=self.y + other.y
            )

        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                point_x=self.x - other.x,
                point_y=self.y - other.y
            )

        return NotImplemented

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            point_x=self.x * other,
            point_y=self.y * other
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length

        return Vector(
            point_x=normalized_x,
            point_y=normalized_y
        )

    def angle_between(self, other_vector: Vector) -> int:
        dot_product = self * other_vector
        magnitude_product = self.get_length() * other_vector.get_length()
        cos_angle = dot_product / magnitude_product

        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)

        return round(abs(angle_degrees))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        rotate_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotate_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(
            point_x=rotate_x,
            point_y=rotate_y
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:

        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]

        return cls(point_x, point_y)
