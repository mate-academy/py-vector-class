from typing import Union
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: Union["Vector", int, float]
    ) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return Vector(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        if self.get_length() != 0:
            return Vector(
                self.x / self.get_length(),
                self.y / self.get_length()
            )
        else:
            return Vector(self.x, self.y)

    def angle_between(self, other: "Vector") -> int:
        cos_a = ((self * other)
                 / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degrees: int) -> "Vector":
        radians_angle = math.radians(degrees)
        new_x = (self.x * math.cos(radians_angle)
                 - self.y * math.sin(radians_angle))
        new_y = (self.x * math.sin(radians_angle)
                 + self.y * math.cos(radians_angle))
        return Vector(round(new_x, 2), round(new_y, 2))
