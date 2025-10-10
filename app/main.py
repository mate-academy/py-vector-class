from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)


    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, num: Vector | int | float) -> float | Vector:
        if isinstance(num, Vector):
            return self.x * num.x + self.y * num.y
        if isinstance(num, (int, float)):
            return Vector(self.x * num, self.y * num)
        raise TypeError("Operand must be Vector, int, or float")

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector | None:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        if length == 0:
            return None
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        len1 = self.get_length()
        len2 = other.get_length()
        cos_theta = dot_product / (len1 * len2)
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        if angle < 0:
            angle += 360
        if angle > 180:
            angle = 360 - angle
        return round(angle)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
