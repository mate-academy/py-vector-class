from __future__ import annotations
import math


class Vector:
    def __init__(self, x_dot: int | float, y_dot: int | float) -> None:
        self.x = round(x_dot, 2)
        self.y = round(y_dot, 2)

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

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if not isinstance(other, (type(self), int, float)):
            assert TypeError(
                "Wrong data type for *: "
                f"'{type(other).__name__} can't be multiplied by 'Vector'"
            )
        if isinstance(other, (int | float)):
            return Vector(
                self.x * other,
                self.y * other
            )

        dot_product = self.x * other.x + self.y * other.y
        return dot_product

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        scalar = self * vector
        v1_len = self.get_length()
        v2_len = vector.get_length()
        return round(math.degrees(math.acos(
            scalar / (v1_len * v2_len)
        )))

    def get_angle(self) -> int:
        sin_a = self.y / self.get_length()
        angle = math.degrees(math.acos(sin_a))
        return round(angle)

    def rotate(self, angle: int) -> Vector:
        vector_x = (self.x * math.cos(math.radians(angle))
                    - self.y * math.sin(math.radians(angle)))
        vector_y = (self.x * math.sin(math.radians(angle))
                    + self.y * math.cos(math.radians(angle)))
        return Vector(vector_x, vector_y)
