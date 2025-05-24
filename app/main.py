from __future__ import annotations
from decimal import Decimal, ROUND_HALF_UP
from math import cos, sin, radians, degrees, acos



class Vector:
    def __init__(self, x: Decimal, y: Decimal) -> None:
        self.x = float(Decimal(str(x)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        self.y = float(Decimal(str(y)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

    def __add__(self, other) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number: Decimal | Vector | int | float) -> Vector | Decimal:
        if isinstance(number, Vector):
            return self.x * number.x + self.y * number.y
        if isinstance(number, (int, float, Decimal)):
            return Vector(self.x * number, self.y * number)
        raise TypeError(f"wrong type of number: {type(number)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> Decimal:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        len_vector = self.get_length()
        return Vector(self.x / len_vector, self.y / len_vector)

    def angle_between(self, other):
        skal = self.x * other.x + self.y * other.y
        cos_a = skal / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return round(degrees(acos(cos_a)))
    def rotate(self, angle: int) -> "Vector":
        rad = radians(angle)
        new_x = self.x * cos(rad) - self.y * sin(rad)
        new_y = self.x * sin(rad) + self.y * cos(rad)
        return Vector(new_x, new_y)
