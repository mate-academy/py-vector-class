from __future__ import annotations
import math


class Vector:
    def __init__(self, vect_x: int | float, vect_y: int | float) -> None:
        self.x = round(vect_x, 2)
        self.y = round(vect_y, 2)

    def __add__(self, other: Vector) -> Vector:
        add_x = self.x + other.x
        add_y = self.y + other.y
        return Vector(add_x, add_y)

    def __sub__(self, other: Vector) -> Vector:
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, float | int):
            mul_x = self.x * other
            mul_y = self.y * other
            return Vector(mul_x, mul_y)
        else:
            mul_x = self.x * other.x
            mul_y = self.y * other.y
            return mul_x + mul_y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        created_x = end_point[0] - start_point[0]
        created_y = end_point[1] - start_point[1]
        return cls(created_x, created_y)

    def get_length(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> Vector:
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector: Vector) -> float:
        own_length = self.get_length()
        other_length = vector.get_length()
        dot_product = self * vector
        cos_a = dot_product / (own_length * other_length)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        vector = Vector(0, abs(self.y))
        return self.angle_between(vector)

    def rotate(self, degrees: int) -> Vector:
        rotated_x = math.cos(math.radians(degrees)) * self.x - \
            math.sin(math.radians(degrees)) * self.y
        rotated_y = math.sin(math.radians(degrees)) * self.x + \
            math.cos(math.radians(degrees)) * self.y
        return Vector(rotated_x, rotated_y)


vector1 = Vector(-3, -4)
print(vector1.get_angle())
