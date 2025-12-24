from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other_v: Vector) -> Vector:
        return Vector(x_coordinate=self.x + other_v.x ,
                      y_coordinate=self.y + other_v.y)

    def __sub__(self, other_v: Vector) -> Vector:
        return Vector(x_coordinate=self.x - other_v.x,
                      y_coordinate=self.y - other_v.y)

    def __mul__(self, other_v: Vector | float | int) -> Vector | float:
        if isinstance(other_v, (float, int)):
            return Vector(x_coordinate=self.x * other_v,
                          y_coordinate=self.y * other_v)
        return self.x * other_v.x + self.y * other_v.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        return Vector(x_coordinate=end_point[0] - start_point[0],
                      y_coordinate=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        len_of_vector = self.get_length()
        return Vector(x_coordinate=self.x / len_of_vector,
                      y_coordinate=self.y / len_of_vector)

    def angle_between(self, other_v: Vector) -> int:
        dot_product = self * other_v

        self_len = self.get_length()
        other_v_len = other_v.get_length()

        cos_of_angle = dot_product / (self_len * other_v_len)
        angle_rad = math.acos(cos_of_angle)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0

        cos_angle = self.y / length
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)

        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)

        return Vector(x_coordinate=new_x,
                      y_coordinate=new_y)
