import math
from typing import Union


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(
            self,
            other: Union[int, float, "Vector"]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[-1] - start_point[-1])

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        magnitude = self.get_length()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.__mul__(other)
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        if magnitude_self == 0 or magnitude_other == 0:
            raise ValueError("Cannot compute angle with zero-length vector")
        cos_angle = dot_product / (magnitude_self * magnitude_other)
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
