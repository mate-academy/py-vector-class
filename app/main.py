import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union[float, int, "Vector"]
    ) -> Union["Vector", float]:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        diff_x = end_point[0] - start_point[0]
        diff_y = end_point[1] - start_point[1]
        return cls(diff_x, diff_y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        dot_product: float = self * vector
        lengths = self.get_length() * vector.get_length()

        if lengths == 0:
            return 0
        cos_a = dot_product / lengths
        cos_a = max(min(cos_a, 1), -1)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_a = self.y / length
        cos_a = max(min(cos_a, 1), -1)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
