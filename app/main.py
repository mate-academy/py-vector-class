from typing import Union, Tuple
import math


class Vector:
    def __init__(self,
                 x_value: Union[int, float],
                 y_value: Union[int, float]) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Union["Vector", int, float]) -> float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        x_component = round(end_point[0] - start_point[0], 2)
        y_component = round(end_point[1] - start_point[1], 2)
        return cls(x_component, y_component)

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 15)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()

        cos_angle = dot_product / (length_self * length_other)

        cos_angle = max(-1, min(1, cos_angle))
        angle = math.degrees(math.acos(cos_angle))

        return round(angle)

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.x, self.y))
        return abs(round(angle))

    def rotate(self, degrees: int) -> "Vector":

        radians = math.radians(degrees)

        x_new = round(
            self.x * math.cos(radians) - self.y * math.sin(radians), 2
        )
        y_new = round(
            self.x * math.sin(radians) + self.y * math.cos(radians), 2
        )

        return Vector(x_new, y_new)
