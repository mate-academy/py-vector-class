import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_coord_x = self.coord_x + other.coord_x
        new_coord_y = self.coord_y + other.coord_y
        return Vector(new_coord_x, new_coord_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_coord_x = self.coord_x - other.coord_x
        new_coord_y = self.coord_y - other.coord_y
        return Vector(new_coord_x, new_coord_y)

    def __mul__(
            self,
            other: Union[int, float, "Vector"]
    ) -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.coord_x * other, self.coord_y * other)
        elif isinstance(other, Vector):
            return (
                self.coord_x * other.coord_x
                + self.coord_y * other.coord_y
            )
        else:
            raise TypeError(
                "Multiplication supported only with int, float, or Vector"
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        new_coord_x = end_point[0] - start_point[0]
        new_coord_y = end_point[1] - start_point[1]
        return cls(new_coord_x, new_coord_y)

    def get_length(self) -> float:
        return (self.coord_x ** 2 + self.coord_y ** 2) ** 0.5

    def angle_between(self, other: "Vector") -> int:
        dot_product = (
            self.coord_x * other.coord_x
            + self.coord_y * other.coord_y
        )
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ZeroDivisionError()

        cos_theta = dot_product / (length_self * length_other)
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.coord_x, self.coord_y)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_coord_x = (
            self.coord_x * math.cos(radians)
            - self.coord_y * math.sin(radians)
        )
        new_coord_y = (
            self.coord_x * math.sin(radians)
            + self.coord_y * math.cos(radians)
        )
        return Vector(new_coord_x, new_coord_y)
