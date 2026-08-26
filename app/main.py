from __future__ import annotations
import math


class Vector:
    def __init__(self, get_x: float, get_y: float) -> None:
        self.x = round(get_x, 2)
        self.y = round(get_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> None:
        lenth = self.get_length()
        return Vector(self.x / lenth, self.y / lenth)

    def angle_between(self, other: Vector) -> int:
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            return 0

        dot_product = self * other
        cos_theta = dot_product / (length_self * length_other)

        cos_theta = max(-1, min(1, cos_theta))

        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg, 0)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))

    def get_angle(self) -> float:
        if self.x == 0 and self.y == 0:
            raise ValueError("Cannot determine the angle of a zero vector.")
        elif self.x == 0 and self.y > 0:
            return 0
        elif self.x == 0 and self.y < 0:
            return 180

        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)

        if angle_deg >= -90 and angle_deg <= 90:
            angle_from_y = (90 - angle_deg) % 360
        else:
            angle_from_y = (450 - angle_deg) % 360

        if angle_from_y > 180:
            angle_from_y = 360 - angle_from_y

        return round(angle_from_y, 0)
