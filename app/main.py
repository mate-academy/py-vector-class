import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        result_x = self.x + other.x
        result_y = self.y + other.y
        return Vector(result_x, result_y)

    def __sub__(self, other: "Vector") -> "Vector":
        result_x = self.x - other.x
        result_y = self.y - other.y
        return Vector(result_x, result_y)

    def __mul__(
            self, other: Union[int, float, "Vector"]
    ) -> Union[int, float, "Vector"]:
        if isinstance(other, (int, float)):
            result_x = self.x * other
            result_y = self.y * other
            return Vector(result_x, result_y)
        if isinstance(other, Vector):
            return ((self.x * other.x)
                    + (self.y * other.y))

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return (cls(end_point[0], end_point[1])
                - cls(start_point[0], start_point[1]))

    def get_length(self) -> float | int:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        vector_length = self.get_length()
        if vector_length == 0:
            return Vector(0, 0)
        else:
            return Vector(
                self.x / vector_length,
                self.y / vector_length
            )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        vector1_length = self.get_length()
        vector2_length = vector.get_length()

        if vector1_length == 0 or vector2_length == 0:
            return 0

        cos_a = dot_product / (vector1_length * vector2_length)
        cos_a = math.degrees(math.acos(cos_a))
        return int(round(cos_a))

    def get_angle(self) -> int:
        y_component = self.get_length()

        if y_component == 0:
            return 0

        degree_angle = math.degrees(math.acos(self.y / y_component))
        return int(round(degree_angle))

    def rotate(self, degrees: int) -> "Vector":
        radian_angle = math.radians(degrees)
        rotated_x = (self.x * math.cos(radian_angle)
                     - self.y * math.sin(radian_angle))
        rotated_y = (self.x * math.sin(radian_angle)
                     + self.y * math.cos(radian_angle))
        return Vector(rotated_x, rotated_y)
