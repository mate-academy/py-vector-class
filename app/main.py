from __future__ import annotations
import math


class Vector:
    def __init__(self, position_x: float, position_y: float) -> None:
        self.x = round(position_x, 2)
        self.y = round(position_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

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

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        norm_of_vector = self.get_length()

        if norm_of_vector == 0:
            return Vector(0, 0)

        normalized_x = round((self.x / norm_of_vector), 2)
        normalized_y = round((self.y / norm_of_vector), 2)

        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector: Vector) -> int:
        return math.ceil(
            math.degrees(
                math.acos(
                    self * vector / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return abs(int(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = round(
            self.x * math.cos(radians)
            - self.y * math.sin(radians),
            2
        )
        new_y = round(
            self.x * math.sin(radians)
            + self.y * math.cos(radians),
            2
        )

        rotated_vector = Vector(new_x, new_y)
        return rotated_vector
