from __future__ import annotations
import math


class Vector:

    def __init__(self, х_coord: int or float, y_coord: int or float) -> None:
        self.x = round(х_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if type(other) == Vector:
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        return Vector(
            self.x + other,
            self.y + other
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector:
        if type(other) == Vector:
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(х_coord=end_point[0] - start_point[0],
                   y_coord=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        return round(math.degrees(
            math.acos(self * vector
                      / (self.get_length()
                         * vector.get_length()))))

    def get_angle(self) -> int:
        if self.x == 0:
            return 0
        elif self.x < 0:
            vector2 = Vector(0, self.x * (-1))
            return round(math.degrees(
                math.acos(self * vector2
                          / (self.get_length()
                             * vector2.get_length()))))
        else:
            vector2 = Vector(0, self.x)
            return round(math.degrees(
                math.acos(self * vector2
                          / (self.get_length()
                             * vector2.get_length()))))

    def rotate(self, degrees: int) -> Vector:
        angle_cos = math.cos(math.radians(degrees))
        angle_sin = math.sin(math.radians(degrees))

        return Vector((self.x * angle_cos - angle_sin * self.y)
                      , (self.x * angle_sin + angle_cos * self.y))
