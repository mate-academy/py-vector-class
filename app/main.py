import math
from typing import Union


class Vector:
    def __init__(self, x_input: float, y_input: float) -> None:
        self.x = round(x_input, 2)
        self.y = round(y_input, 2)

    def __add__(self: "Vector", other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self: "Vector", other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self: "Vector",
        other: Union[float, "Vector"]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls: "Vector",
        start: tuple,
        end: tuple
    ) -> "Vector":

        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self: "Vector") -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self: "Vector") -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self: "Vector", other: "Vector") -> float:
        coords_sum = self.x * other.x + self.y * other.y
        len_mul = self.get_length() * other.get_length()
        cos_a = coords_sum / len_mul

        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self: "Vector") -> float:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)

        return round(abs(angle_degrees))

    def rotate(self: "Vector", degrees: int) -> "Vector":
        radians = math.radians(degrees)
        return Vector(self.x * math.cos(radians) - self.y * math.sin(radians),
                      self.x * math.sin(radians) + self.y * math.cos(radians))
