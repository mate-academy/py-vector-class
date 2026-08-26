from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_value=self.x + other.x,
                y_value=self.y + other.y
            )
        return Vector(
            x_value=self.x + other,
            y_value=self.y + other
        )

    def __sub__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_value=self.x - other.x,
                y_value=self.y - other.y
            )
        return Vector(
            x_value=self.x - other,
            y_value=self.y - other
        )

    def __mul__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_value=self.x * other,
            y_value=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_value = end_point[0] - start_point[0]
        y_value = end_point[1] - start_point[1]
        return cls(x_value, y_value)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(
            x_value=normalized_x,
            y_value=normalized_y
        )

    def angle_between(self, other: Vector) -> int:
        cosine_theta = (self.x * other.x
                        + self.y * other.y) / (self.get_length()
                                               * other.get_length())
        theta_rad = math.acos(cosine_theta)
        theta_deg = round(math.degrees(theta_rad))
        return theta_deg

    def get_angle(self) -> int:
        positive_y = Vector(x_value=0, y_value=1)
        return self.angle_between(positive_y)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(
            x_value=rotated_x,
            y_value=rotated_y
        )
