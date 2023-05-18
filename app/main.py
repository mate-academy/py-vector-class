from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_point_x, start_point_y = start_point
        end_point_x, end_point_y = end_point
        return Vector(end_point_x - start_point_x, end_point_y - start_point_y)

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        normal = (self.x ** 2 + self.y ** 2) ** 0.5
        x_coordinate = self.x / normal
        y_coordinate = self.y / normal
        return Vector(x_coordinate, y_coordinate)

    def angle_between(self, vector2: Vector) -> int:
        multiplying = self.x * vector2.x + self.y * vector2.y
        module_vector1 = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        module_vector2 = ((vector2.x ** 2) + (vector2.y ** 2)) ** 0.5
        cos_a = multiplying / (module_vector1 * module_vector2)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        degrees_in_radians = math.radians(degrees)
        x_coordinate = self.x * math.cos(degrees_in_radians) - \
            self.y * math.sin(degrees_in_radians)
        y_coordinate = self.y * math.cos(degrees_in_radians) + \
            self.x * math.sin(degrees_in_radians)
        return Vector(x_coordinate, y_coordinate)
