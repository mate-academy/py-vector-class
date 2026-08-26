from __future__ import annotations
import math


class Vector:

    def __init__(self, x_vector: int | Vector, y_vector: int | Vector) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError(f"Cannot add {type(other)} with {type(Vector)}")

    def __sub__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        else:
            raise TypeError(f"Cannot subtract "
                            f"{type(other)} with {type(Vector)}")

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(f"Cannot multiply "
                            f"{type(other)} with {type(Vector)}")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: int | float, end_point: int | float
    ) -> Vector:
        if len(start_point) != 2 or len(end_point) != 2:
            raise ValueError("Both points must have exactly 2 coordinates")
            # new_x = x2 - x1  #new_y = y2 = y1
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        rounded_length = round(length, 2)
        if rounded_length == 0:
            raise ValueError("Cannot normalize zero vector")
        vector = Vector(self.x / length, self.y / length)
        return vector

    def angle_between(self, vector: Vector) -> int:
        dot = self * vector
        length_x = self.get_length()
        length_y = vector.get_length()
        if length_x == 0 or length_y == 0:
            raise ValueError("One of the vectors has zero length")
        cos_a = dot / (length_x * length_y)
        cos_clamp = min(max(cos_a, -1.0), 1.0)
        radians = math.acos(cos_clamp)
        degrees = math.degrees(radians)
        return int(round(degrees))

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            raise ValueError("Zero vector does not have an angle")
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree : int) -> Vector:
        angle_radians = math.radians(degree)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)
        x_prime = (self.x * cos_theta - (self.y * sin_theta))
        y_prime = (self.x * sin_theta + (self.y * cos_theta))
        return Vector(x_prime, y_prime)
