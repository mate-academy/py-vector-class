import math
from typing import Union


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coordinate + other.x_coordinate,
            self.y_coordinate + other.y_coordinate,
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x_coordinate - other.x_coordinate,
            self.y_coordinate - other.y_coordinate,
        )

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return round(
                self.x_coordinate * other.x_coordinate
                + self.y_coordinate * other.y_coordinate,
                4,
            )
        return Vector(
            round(self.x_coordinate * other, 2),
            round(self.y_coordinate * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_coordinate**2 + self.y_coordinate**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x_coordinate / length, 2),
            round(self.y_coordinate / length, 2),
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            return 0
        cos_angle = max(-1.0, min(1.0, dot_product / lengths_product))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x_coordinate = self.x_coordinate * cos_angle - self.y_coordinate * sin_angle
        new_y_coordinate = self.x_coordinate * sin_angle + self.y_coordinate * cos_angle
        return Vector(
            round(new_x_coordinate, 2),
            round(new_y_coordinate, 2),
        )
