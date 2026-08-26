from typing import Any
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Any) -> Any:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Any) -> Any:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (float, int)):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Any:
        return Vector(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Any:
        return Vector(
            x_coord=round(self.x / self.get_length(), 2),
            y_coord=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Any) -> float:
        angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Any:
        rotated_x = self.x * math.cos(math.radians(degrees)) \
            - self.y * math.sin(math.radians(degrees))
        rotated_y = self.x * math.sin(math.radians(degrees)) \
            + self.y * math.cos(math.radians(degrees))
        return Vector(x_coord=rotated_x, y_coord=rotated_y)
