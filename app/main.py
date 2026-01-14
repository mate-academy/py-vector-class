from __future__ import annotations
import math


class Vector:
    def __init__(self, pos_x: float, pos_y: float) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def angle_between(self, other: Vector) -> float:
        cosines = (self * other) / (self.get_length() * other.get_length())
        acosines = math.acos(cosines)
        return round(math.degrees(acosines))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        radians = math.radians(angle)
        x_prime = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_prime = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_prime, 2), round(y_prime, 2))

# Example usage:


vector1 = Vector(3, 4)
vector2 = Vector(1, 2)

result_sum = vector1 + vector2
result_diff = vector1 - vector2
result_scalar_mul = vector1 * 2
result_dot_product = vector1 * vector2


print("Vector 1:", vector1.x, vector1.y)
print("Vector 2:", vector2.x, vector2.y)
print("Sum:", result_sum.x, result_sum.y)
print("Difference:", result_diff.x, result_diff.y)
print("Scalar Multiplication:", result_scalar_mul.x, result_scalar_mul.y)
print("Dot Product:", result_dot_product)
