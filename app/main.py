import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(
                "Można dodawać tylko obiekty Vector do Vector."
            )
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(
                "Można odejmować tylko obiekty Vector od Vector."
            )
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self, other: Union[int, float, "Vector"]
    ) -> Union["Vector", float]:
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
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

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
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError(
                "Cannot calculate angle with a zero-length vector."
            )
        dot_product = self * other
        cosine_angle = dot_product / (len_self * len_other)
        cosine_angle = max(-1.0, min(1.0, cosine_angle))
        angle_rad = math.acos(cosine_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
