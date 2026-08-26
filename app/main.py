from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_coord + other.x_coord,
                      self.y_coord + other.y_coord)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x_coord - other.x_coord,
                      self.y_coord - other.y_coord)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x_coord * other, self.y_coord * other)
        elif isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_start, y_start = start_point
        x_end, y_end = end_point
        x_coord = x_end - x_start
        y_coord = y_end - y_start
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x_coord ** 2 + self.y_coord ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x_coord / length, self.y_coord / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_a = dot_product / (length_self * length_other)
        cos_a = max(-1.0, min(1.0, cos_a))

        angle_deg = math.degrees(math.acos(cos_a))

        return round(angle_deg)

    def get_angle(self) -> int:
        unit_vector_y = Vector(0, 1)
        dot_product = self * unit_vector_y
        length_self = self.get_length()
        length_unit_y = unit_vector_y.get_length()
        cos_theta = dot_product / (length_self * length_unit_y)
        angle_deg = math.degrees(math.acos(cos_theta))
        if self.x_coord > 0:
            angle_deg = 360 - angle_deg
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        x_new = self.x_coord * cos_theta - self.y_coord * sin_theta
        y_new = self.x_coord * sin_theta + self.y_coord * cos_theta

        return Vector(x_new, y_new)
