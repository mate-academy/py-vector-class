from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_point = list(start_point)
        end_point = list(end_point)
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        numerator = self.__mul__(other)
        denominator = self.get_length() * other.get_length()
        result = math.degrees(math.acos(numerator / denominator))
        return int(round(result, 0))

    def get_angle(self) -> int:
        result = math.degrees(math.acos(self.y / self.get_length()))
        return int(round(result, 0))

    def rotate(self, angle: int) -> Vector:
        rotate_angle = math.radians(angle)
        return Vector(self.x * math.cos(rotate_angle)
                      - self.y * math.sin(rotate_angle),
                      self.x * math.sin(rotate_angle)
                      + self.y * math.cos(rotate_angle))
