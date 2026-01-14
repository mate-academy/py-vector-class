from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: list, end_point: list
    ) -> Vector:
        return Vector(
            x_coord=(end_point[0] - start_point[0]),
            y_coord=(end_point[1] - start_point[1])
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=self.x / self.get_length(),
            y_coord=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        oy = Vector(0, 1)
        cos_a = (self * oy) / (self.get_length() * oy.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        """
        x` = x*cos(angle) - y*sin(angle)
        y` = x*sin(angle) + y*cos(angle)
        """
        teta = math.radians(angle)
        vector_x = self.x * math.cos(teta) - self.y * math.sin(teta)
        vector_y = self.x * math.sin(teta) + self.y * math.cos(teta)
        return Vector(
            x_coord=vector_x,
            y_coord=vector_y
        )
