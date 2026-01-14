from typing import Union
from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(x_coord=other.x + self.x, y_coord=other.y + self.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(x_coord=self.x - other.x, y_coord=self.y - other.y)

    def __mul__(self,
                other: Union[float, int, "Vector"],
                ) -> Union[float, "Vector"]:
        if isinstance(other, (float, int)):
            return Vector(x_coord=self.x * other, y_coord=self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(x_coord=self.x / length, y_coord=self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_between = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_between)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(x_coord=0, y_coord=1))

    def rotate(self, degrees: int) -> "Vector":
        degrees = radians(degrees)
        return Vector(
            x_coord=(self.x * cos(degrees) - self.y * sin(degrees)),
            y_coord=(self.x * sin(degrees) + self.y * cos(degrees)),
        )
