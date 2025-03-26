from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_value = end_point[0] - start_point[0]
        y_value = end_point[1] - start_point[1]
        return Vector(round(x_value, 2), round(y_value, 2))

    def get_length(self) -> float:
        # Calculate length (mod) of vector
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)  # cancel div to 0
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_prod = self.__mul__(other)
        length_self = self.get_length()
        length_other = other.get_length()
        # cancel when length vectors = 0
        if length_self == 0 or length_other == 0:
            return 0
        cos_theta = dot_prod / (length_self * length_other)
        # Prevent rounding errors by limiting the value of cos_theta to [-1, 1]
        cos_theta = max(-1, min(1, cos_theta))
        # take answer in rad
        angle_rad = math.acos(cos_theta)
        # convert to degrees
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            return 0  # Zero vector case

        # Calculate angle with the positive Y-axis
        angle = math.degrees(math.atan(abs(self.x) / abs(self.y)))

        if self.x < 0 and self.y < 0:
            angle = 180 - angle  # for 4 quadrant
        elif self.x > 0 > self.y:
            angle += 180  # for third quadrant
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)  # Convert degrees to rad
        rotated_x = round(
            self.x * math.cos(radians) - self.y * math.sin(radians
                                                           ), 2)
        rotated_y = round(
            self.x * math.sin(radians) + self.y * math.cos(radians
                                                           ), 2)
        return Vector(rotated_x, rotated_y)
