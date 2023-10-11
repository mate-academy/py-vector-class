from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        return Vector(self.x / vector_len, self.y / vector_len)

    def angle_between(self, other: Vector) -> float:
        multiplication = self.__mul__(other)
        length_total = self.get_length() * other.get_length()
        cos_a = multiplication / length_total
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        vector_y = Vector(0, 1)
        return round(self.angle_between(vector_y))

    def rotate(self, degrees: int) -> Vector:
        degr_rad = math.radians(degrees)
        x_vect = self.x * math.cos(degr_rad) - self.y * math.sin(degr_rad)
        y_vect = self.x * math.sin(degr_rad) + self.y * math.cos(degr_rad)
        return Vector(round(x_vect, 2), round(y_vect, 2))
