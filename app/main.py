from __future__ import annotations
import math


class Vector:

    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other_vector: Vector) -> Vector:
        if isinstance(other_vector, Vector):
            return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: Vector) -> Vector:
        if isinstance(other_vector, Vector):
            return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, other_vector: int | float | Vector) -> Vector | float:
        if isinstance(other_vector, (float, int)):
            return Vector(self.x * other_vector, self.y * other_vector)
        elif isinstance(other_vector, Vector):
            return self.x * other_vector.x + self.y * other_vector.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: float,
                                    end_point: float) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector: Vector) -> int:
        dot_prod = self * other_vector
        cos_a = dot_prod / (self.get_length() * other_vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
