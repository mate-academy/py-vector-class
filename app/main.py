from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )

        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )

        return NotImplemented

    def __mul__(self, other: "Vector | int | float") -> "Vector | int | float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )

        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        sum_of_squares = self.x ** 2 + self.y ** 2
        return math.sqrt(sum_of_squares)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: "Vector") -> int:
        multiplied_vectors = (
            self.x * other.x
            + self.y * other.y
        )

        length_1 = self.get_length()
        length_2 = other.get_length()

        cosine = multiplied_vectors / (length_1 * length_2)
        cosine = max(-1, min(1, cosine))

        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        rotated_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )
        rotated_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(rotated_x, rotated_y)
