from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: (int, float), y_coord: (int, float)) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)

    def __mul__(self, other: (Vector, int, float)) -> (Vector, int, float):
        if isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> (int, float):
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x_normalized = self.x / length
        y_normalized = self.y / length
        return Vector(x_normalized, y_normalized)

    def angle_between(self, other: Vector) -> (int, float):
        return round(
            math.degrees(
                math.acos(
                    (self.x * other.x + self.y * other.y)
                    / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> (int, float):
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, angle: (int, float)) -> Vector:
        angle_radians = math.radians(angle)
        x_rotate = self.x * math.cos(angle_radians) - self.y * math.sin(
            angle_radians
        )
        y_rotate = self.x * math.sin(angle_radians) + self.y * math.cos(
            angle_radians
        )
        return Vector(x_rotate, y_rotate)
