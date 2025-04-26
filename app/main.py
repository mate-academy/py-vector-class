from __future__ import annotations
import math


class Vector:
    def __init__(self, cord_x: float, cord_y: float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, sum_vector: Vector) -> Vector:
        return Vector(self.x + sum_vector.x, self.y + sum_vector.y)

    def __sub__(self, sub_vector: Vector) -> Vector:
        return Vector(self.x - sub_vector.x, self.y - sub_vector.y)

    def __mul__(self, mul_vector: float | int | Vector) -> Vector:
        if isinstance(mul_vector, Vector):
            return (self.x * mul_vector.x) + (self.y * mul_vector.y)
        return Vector(self.x * mul_vector, self.y * mul_vector)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        result = Vector(end_point[0],
                        end_point[1]) - Vector(start_point[0], start_point[1])
        return result

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        cord_x = self.x / self.get_length()
        cord_y = self.y / self.get_length()
        return Vector(cord_x, cord_y)

    def angle_between(self, vector: Vector) -> int | float:
        scalar = (self.x * vector.x) + (self.y * vector.y)
        norma_x = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        norma_y = ((vector.x ** 2) + (vector.y ** 2)) ** 0.5
        cos = scalar / (norma_x * norma_y)
        acos = math.acos(cos)
        graus = math.degrees(acos)
        return round(graus)

    def get_angle(self) -> int | float:
        angle_in_radians = math.atan2(self.x, self.y)
        graus = math.degrees(angle_in_radians)
        return round(abs(graus))

    def rotate(self, angle: int | float) -> Vector:
        radians = angle * (3.1415 / 180)
        cord_x = (self.x * math.cos(radians)) - (self.y * math.sin(radians))
        cord_y = (self.x * math.sin(radians)) + (self.y * math.cos(radians))
        return Vector(cord_x, cord_y)
