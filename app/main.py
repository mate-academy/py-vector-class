from __future__ import annotations
import math


class Vector:

    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.x == 0:
            return Vector(0, 1)
        if self.y == 0:
            return Vector(1, 0)
        if self.x < 0:
            x_normalized = - math.sqrt(1 / ((self.y / self.x) ** 2 + 1))
        else:
            x_normalized = math.sqrt(1 / ((self.y / self.x) ** 2 + 1))
        if self.y < 0:
            y_normalized = - math.sqrt(1 / ((self.x / self.y) ** 2 + 1))
        else:
            y_normalized = math.sqrt(1 / ((self.x / self.y) ** 2 + 1))
        return Vector(x_normalized, y_normalized)

    def angle_between(self, other: Vector) -> int | float:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int | float:
        cos_angle = (self * Vector(0, 1)) / (self.get_length() * 1)
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, angle: int | float) -> Vector:
        cos_angle_self_x = (self * Vector(1, 0)) / (self.get_length() * 1)
        angle_self_x = math.degrees(math.acos(cos_angle_self_x))
        # кут між віссю Х і вектором self

        if self.y < 0:
            angle_self_x = 360 - angle_self_x
            # кут між віссю Х і вектором self в полярній системі координат

        angle_x = angle_self_x + angle
        # кут між віссю Х і повернутим вектором в полярній системі координат

        x_roteted = self.get_length() * math.cos(math.radians(angle_x))
        y_roteted = self.get_length() * math.sin(math.radians(angle_x))
        return Vector(x_roteted, y_roteted)
