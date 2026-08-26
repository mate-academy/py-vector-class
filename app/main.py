import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

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
        other: Union[int, float, "Vector"],
    ) -> Union["Vector", float]:
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
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        if length == 0:
            return Vector(0, 0)

        return Vector(
            self.x / length,
            self.y / length,
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        length_self = self.get_length()
        length_other = vector.get_length()
        cos_value = dot_product / (length_self * length_other)
        angle = math.degrees(math.acos(cos_value))
        return round(angle)

    def get_angle(self) -> int:
        length = self.get_length()
        cos_value = self.y / length
        angle = math.degrees(math.acos(cos_value))
        return round(angle)

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
