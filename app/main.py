from __future__ import annotations

import math


class Vector:
    # write your code here
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)
        return self

    def __mul__(self, other: Vector | float) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = Vector.get_length(self)
        return Vector(self.x / length, self.y / length)

    def get_angle(self) -> int:
        v2 = Vector(0, abs(self.y))
        return round(math.degrees(
            math.acos((self * v2) / (Vector.get_length(self)
                                     * Vector.get_length(v2)))))

    def angle_between(self, other: Vector) -> int:
        v2 = Vector(other.x, other.y)
        return math.ceil(
            math.degrees(
                math.acos((self * v2) / (Vector.get_length(self)
                                         * Vector.get_length(v2)))))

    def rotate(self, degrees: int) -> Vector:
        ox, oy = 0, 0
        px, py = self.x, self.y
        angle = math.radians(degrees)

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        return Vector(qx, qy)
