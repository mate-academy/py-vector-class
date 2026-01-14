from typing import Union
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    @classmethod
    def create_vector_by_two_points(
            cls,
            point1: tuple,
            point2: tuple
    ) -> "Vector":
        x_coordinate = round(point2[0] - point1[0], 2)
        y_coordinate = round(point2[1] - point1[1], 2)
        return cls(x_coordinate, y_coordinate)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(
                f"unsupported operand type(s) for +: 'Vector' and "
                f"{type(other)}"
            )
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError(
                f"unsupported operand type(s) for -: 'Vector' and "
                f"{type(other)}"
            )
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union["Vector", int, float]
    ) -> Union["Vector", float]:
        if not isinstance(other, Vector):
            if isinstance(other, int | float):
                return Vector(
                    round(self.x * other, 2),
                    round(self.y * other, 2)
                )
            raise TypeError(
                f"unsupported operand type(s) for *: 'Vector' and "
                f"{type(other)}"
            )
        return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1, min(1, cos_theta))
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        return -round(math.degrees(angle_radians))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
