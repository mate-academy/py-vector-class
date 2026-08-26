from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x
                    + self.y * other.y)
        else:
            return Vector(self.x * other,
                          self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2
                         + self.y ** 2)

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length,
                      self.y * inv_length)

    def angle_between(self, vector: Vector) -> int:
        first = (self.x * vector.x
                 + self.y * vector.y)
        second = (math.sqrt(self.x ** 2
                            + self.y ** 2)
                  * math.sqrt(vector.x ** 2
                              + vector.y ** 2))
        cos_a = first / second
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        angle_radians = math.radians(degrees)
        x2 = round(self.x * math.cos(angle_radians)
                   - self.y * math.sin(angle_radians), 2)
        y2 = round(self.x * math.sin(angle_radians)
                   + self.y * math.cos(angle_radians), 2)
        return Vector(x2, y2)
