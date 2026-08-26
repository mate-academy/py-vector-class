import math
from typing import Union


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    @property
    def x(self) -> float:
        return self.x_coordinate

    @property
    def y(self) -> float:
        return self.y_coordinate

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x_coordinate + other.x_coordinate
            new_y = self.y_coordinate + other.y_coordinate
            return Vector(new_x, new_y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x_coordinate - other.x_coordinate
            new_y = self.y_coordinate - other.y_coordinate
            return Vector(new_x, new_y)
        return NotImplemented

    def __mul__(
        self, other: Union[int, float, "Vector"]
    ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            dot_product = (
                self.x_coordinate * other.x_coordinate
                + self.y_coordinate * other.y_coordinate
            )
            return dot_product
        if isinstance(other, (int, float)):
            scaled_x = self.x_coordinate * other
            scaled_y = self.y_coordinate * other
            return Vector(scaled_x, scaled_y)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        return math.sqrt(
            self.x_coordinate ** 2 + self.y_coordinate ** 2
        )

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = self.x_coordinate / length
        normalized_y = self.y_coordinate / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = (
            self.x_coordinate * other.x_coordinate
            + self.y_coordinate * other.y_coordinate
        )
        length_self = self.get_length()
        length_other = other.get_length()
        cos_angle = dot_product / (length_self * length_other)
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)

    def get_angle(self) -> int:
        dot_product = self.y_coordinate  # скаляр с (0,1)
        length = self.get_length()
        cos_angle = dot_product / length
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)

    def rotate(self, degrees: Union[int, float]) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = (
            self.x_coordinate * math.cos(radians)
            - self.y_coordinate * math.sin(radians)
        )
        rotated_y = (
            self.x_coordinate * math.sin(radians)
            + self.y_coordinate * math.cos(radians)
        )
        return Vector(rotated_x, rotated_y)
