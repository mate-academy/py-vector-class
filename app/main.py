from __future__ import annotations
import math


class Vector:
    def __init__(self, dx: float, dy: float) -> None:
        self.x = round(dx, 2)
        self.y = round(dy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(dx=self.x + other.x, dy=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(dx=self.x - other.x, dy=self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(dx=self.x * other, dy=self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple,
                                    ) -> Vector:
        return Vector(
            dx=end_point[0] - start_point[0],
            dy=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = Vector.get_length(self)
        if length != 0:
            return Vector(
                dx=self.x / length,
                dy=self.y / length,
            )
        raise ValueError("The zero vector cannot be normalized!")

    def angle_between(self, other: Vector) -> int:
        len_self = Vector.get_length(self)
        len_other = Vector.get_length(other)
        if len_self == 0 and len_other == 0:
            raise ValueError()
        cos_a = (self * other) / (len_self * len_other)

        return round((math.degrees(math.acos(cos_a))))

    def get_angle(self) -> int:
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta

        return Vector(dx=new_x, dy=new_y)
