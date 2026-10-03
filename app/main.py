import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(
        self,
        other: Union["Vector", int, float],
    ) -> Union["Vector", int, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple,
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(
            self.x / length,
            self.y / length,
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        lengths = self.get_length() * vector.get_length()
        cos_a = dot_product / lengths

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        return self.angle_between(positive_y)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )
        new_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(new_x, new_y)
