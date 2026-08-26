import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self._coord_x = round(coord_x, 2)
        self._coord_y = round(coord_y, 2)

    @property
    def x(self) -> float:
        return self._coord_x

    @property
    def y(self) -> float:
        return self._coord_y

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
    self, other: Union[int, float, "Vector"]
) -> Union["Vector", float]:
    if isinstance(other, (int, float)):
        return Vector(
            round(self.x * other, 2), round(self.y * other, 2)
        )
    elif isinstance(other, Vector):
        dot_product = round(self.x * other.x + self.y * other.y, 3)  # Rounded to 3 decimal places
        return dot_product
    return NotImplemented


    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2), round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector.")

        cos_angle = dot_product / (len_self * len_other)
        angle_degrees = math.degrees(math.acos(max(-1, min(1, cos_angle))))
        return round(angle_degrees)

    def get_angle(self) -> int:
        vertical_vector = Vector(0, 1)
        return self.angle_between(vertical_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(rotated_x, 2), round(rotated_y, 2))

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
