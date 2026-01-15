from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (float, int)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                "Unsupported operand type(s) for *: 'Vector' and '{}'"
                .format(type(other).__name__)
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        norm_x = self.x / length
        norm_y = self.y / length
        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> float:
        length_s = self.get_length()
        length_o = other.get_length()
        cos_a = (self * other) / (length_s * length_o)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self, ) -> float:
        positive_y_axis = Vector(0, 1)
        cos_a = ((self * positive_y_axis)
                 / (self.get_length() * positive_y_axis.get_length()))
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
