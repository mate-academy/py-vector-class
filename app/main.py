from typing import Union
from math import sqrt, cos, degrees, acos, sin, radians, atan2


class Vector:
    def __init__(
        self, coord_x: Union[int, float], coord_y: Union[int, float]
    ) -> None:  # NOQA E501
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: Union[int, float]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Union[int, float]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union[int, float, "Vector"]
    ) -> Union["Vector", int, float]:  # NOQA E501
        if (
            self.x == 0
            or self.y == 0
            or (isinstance(other, Vector) and (other.x == 0 or other.y == 0))
        ):  # NOQA E501
            return 0
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":  # NOQA E501
        start_x, start_y = start_point
        end_x, end_y = end_point
        coordinates_x = end_x - start_x
        coordinates_y = end_y - start_y
        return Vector(coordinates_x, coordinates_y)

    def get_length(self) -> float:
        vector_length = sqrt(self.x * self.x + self.y * self.y)
        return abs(vector_length)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized = Vector(self.x / length, self.y / length)
        return normalized

    def angle_between(self, other: "Vector") -> float:
        scalar_product_of_vectors = self.x * other.x + self.y * other.y
        vector_model_length = self.get_length() * other.get_length()
        return int(
            round(degrees(acos(scalar_product_of_vectors / vector_model_length)), 0) # NOQA E501
        )  # NOQA E501

    def get_angle(self) -> float:
        if self.x == 0 or self.y == 0:
            return 0
        angle = atan2(self.x, self.y)
        angle_degrees = degrees(angle)
        return int(abs(angle_degrees))

    def rotate(self, angle: int) -> "Vector":
        angle_radians = radians(angle)
        rotate_x = self.x * cos(angle_radians) - self.y * sin(angle_radians)
        rotate_y = self.x * sin(angle_radians) + self.y * cos(angle_radians)
        return Vector(rotate_x, rotate_y)
