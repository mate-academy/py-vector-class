from typing import Union
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        x_coordinate = self.x + other.x
        y_coordinate = self.y + other.y
        return Vector(x_coordinate, y_coordinate)

    def __sub__(self, other: "Vector") -> "Vector":
        x_coordinate = self.x - other.x
        y_coordinate = self.y - other.y
        return Vector(x_coordinate, y_coordinate)

    def __mul__(self, other: Union[float, "Vector", int]) -> "Vector":
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        else:
            x_coordinate = self.x * other.x
            y_coordinate = self.y * other.y
            return x_coordinate + y_coordinate

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, second_vector: "Vector") -> float:
        angle_radians = math.acos(
            (self * second_vector) / (self.get_length()
                                      * second_vector.get_length())
        )
        return round(math.degrees(angle_radians))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x_coordinate = (self.x * math.cos(radians)
                            - self.y * math.sin(radians))
        new_y_coordinate = (self.x * math.sin(radians)
                            + self.y * math.cos(radians))

        return Vector(
            round(new_x_coordinate, 2),
            round(new_y_coordinate, 2),
        )
