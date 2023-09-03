from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: any) -> Vector:
        if isinstance(other, (int, float)):
            self.x = self.x + other
            self.y = self.y + other
            return Vector(self.x, self.y)
        else:
            self.x = self.x + other.x
            self.y = self.y + other.y
            return Vector(self.x, self.y)

    def __sub__(self, other: any) -> Vector:
        if isinstance(other, (int, float)):
            self.x = self.x - other
            self.y = self.y - other
            return Vector(self.x, self.y)
        else:
            self.x = self.x - other.x
            self.y = self.y - other.y
            return Vector(self.x, self.y)

    def __mul__(self, other: any) -> Vector:
        if isinstance(other, (int, float)):
            self.x = self.x * other
            self.y = self.y * other
            return Vector(self.x, self.y)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self * other / (self.get_length() * other.get_length())
                )
            ),
            0
        )

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(abs(self.x), abs(self.y)))
        if self.y < 0:
            angle = 180 - angle
        return round(angle, 0)

    def rotate(self, angle: int) -> Vector:
        current_length = self.get_length()
        current_angle = math.degrees(math.atan2(self.y, self.x))
        new_angle = current_angle + angle
        coord_x = round(current_length * math.cos(math.radians(new_angle)), 2)
        coord_y = round(current_length * math.sin(math.radians(new_angle)), 2)
        return Vector(coord_x, coord_y)
