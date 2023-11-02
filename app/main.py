from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x: float = round(x_coordinate, 2)
        self.y: float = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector | float) -> int:
        cos_angle: float = (self * other) / (self.get_length()
                                             * other.get_length())
        angle_in_radians: float = math.acos(cos_angle)
        angle_in_degrees: int = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        return round(math.degrees(math.atan2(-self.x, self.y)))

    def rotate(self, degrees: int) -> Vector:
        radians: float = math.radians(degrees)
        new_x: float = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y: float = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
