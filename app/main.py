import math
from typing import Union


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other: "Vector") -> "Vector":
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other: Union["Vector", float]) -> Union[float, "Vector"]:

        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y

            return x + y

        else:
            x = self.x * other
            y = self.y * other

            return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":

        x1, y1 = start_point
        x2, y2 = end_point
        x = x2 - x1
        y = y2 - y1

        return cls(x, y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        module_vector = self.get_length()
        x = self.x / module_vector
        y = self.y / module_vector

        return Vector(x, y)

    def angle_between(self, other: "Vector") -> int:
        magnitude_vec_1 = self.get_length()
        magnitude_vec_2 = (other.x ** 2 + other.y ** 2) ** 0.5

        dot_product = self * other
        cos0 = dot_product / (magnitude_vec_1 * magnitude_vec_2)

        return math.ceil(math.degrees(math.acos(cos0)))

    def get_angle(self) -> float:
        angle_radians = math.atan2(self.x, self.y)

        return int(math.degrees(angle_radians)) * -1

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(x, y)
