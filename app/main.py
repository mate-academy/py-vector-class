from typing import Union
import math


class Vector:
    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(
            self,
            other: Union[int, float, "Vector"]
    ) -> Union[int, float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> Union[int, float]:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Union["Vector", None]:
        length = self.get_length()
        if length == 0:
            return None
        if isinstance(length, Union[int, float]):
            return Vector(
                round(self.x / length, 2),
                round(self.y / length, 2)
            )

    def angle_between(self, other: "Vector") -> Union[int, float]:
        self_length = (self.x ** 2 + self.y ** 2) ** 0.5
        other_length = (other.x ** 2 + other.y ** 2) ** 0.5
        cosine_angle = (self * other) / (self_length * other_length)
        return round(math.degrees(math.acos(cosine_angle)))

    def get_angle(self) -> Union[int, float]:
        length = self.get_length()
        return round(math.degrees(math.acos(self.y / length)))

    def rotate(self, degrees: Union[int, float]) -> "Vector":
        radians = math.radians(degrees)
        return Vector(
            x=self.x * math.cos(radians) - self.y * math.sin(radians),
            y=self.y * math.cos(radians) + self.x * math.sin(radians)
        )
