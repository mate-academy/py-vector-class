import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Można dodawać tylko obiekty Vector do Vector.")

        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(
                "Można odejmować tylko obiekty Vector od Vector."
            )

        new_x = self.x - other.x
        new_y = self.y - other.y

        return Vector(new_x, new_y)

    def __mul__(self, other) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        else:
            raise TypeError(
                "Wektor można pomnożyć tylko przez liczbę lub inny wektor."
            )

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")

        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        if not isinstance(other, Vector):
            raise TypeError(
                "Can only calculate angle between Vector objects."
            )

        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            raise ValueError(
                "Cannot calculate angle with a zero-length vector."
            )

        cosine_angle = dot_product / (len_self * len_other)
        cosine_angle = max(-1.0, min(1.0, cosine_angle))

        angle_rad = math.acos(cosine_angle)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def get_angle(self) -> int:
        positive_y_axis_vector = Vector(0, 1)
        return self.angle_between(positive_y_axis_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(new_x, new_y)
