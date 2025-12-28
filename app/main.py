from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other,
                          self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        multiplication = self * other
        self_length = self.get_length()
        other_length = other.get_length()
        cos_angle = multiplication / (self_length * other_length)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self, vector_positive_y: tuple = (0, 1)) -> int:
        multiplication = self * Vector(*vector_positive_y)
        self_length = self.get_length()
        positive_y_length = Vector(*vector_positive_y).get_length()
        cos_angle = multiplication / (self_length * positive_y_length)
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, angle: int | float) -> Vector:
        angle_in_radians = math.radians(angle)
        rotated_vector_x = (self.x * math.cos(angle_in_radians)
                            - self.y * math.sin(angle_in_radians))
        rotated_vector_y = (self.x * math.sin(angle_in_radians)
                            + self.y * math.cos(angle_in_radians))
        return Vector(rotated_vector_x, rotated_vector_y)
