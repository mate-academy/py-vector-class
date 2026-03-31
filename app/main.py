from __future__ import annotations

import math

Number = int | float
CoordinatesTuple = tuple[Number, Number]


class Vector:
    def __init__(self, x_value: Number, y_value: Number) -> None:
        self.x = round(float(x_value), 2)
        self.y = round(float(y_value), 2)

    def __str__(self) -> str:
        return f"Vector ({self.x}, {self.y})"

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other: Vector) -> Vector:
        return self.__add__(other)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | Number) -> Vector | Number:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, Number):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls, start_p: CoordinatesTuple, end_p: CoordinatesTuple
    ) -> Vector:
        if not (isinstance(start_p, tuple) and isinstance(end_p, tuple)):
            raise TypeError("Arguments must be tuples of coordinates.")
        if len(start_p) < 2 or len(end_p) < 2:
            raise ValueError("Tuple must contain two coordinates (x, y).")

        start_x, start_y = start_p[:2]
        end_x, end_y = end_p[:2]
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> Number:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if not length > 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> Number:
        if not isinstance(other, Vector):
            raise TypeError("Argument must be type vector.")

        l1 = self.get_length()
        l2 = other.get_length()
        dot_product = (self.x * other.x + self.y * other.y) / (l1 * l2)
        dot_product = max(-1.0, min(1.0, dot_product))
        angle_rad = math.acos(dot_product)
        print(angle_rad)
        angle_deg = math.degrees(angle_rad)
        print(angle_deg)
        return round(angle_deg)

    def get_angle(self) -> Number:
        length = self.get_length()
        if length == 0:
            return 0

        cos_alpha = max(-1.0, min(1.0, self.y / length))
        angle_rad = math.acos(cos_alpha)
        return round(math.degrees(angle_rad))

    def rotate(self, angle_deg: Number) -> Vector:
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
