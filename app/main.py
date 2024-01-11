from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x: float = round(x_point, 2)
        self.y: float = round(y_point, 2)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, endp: tuple) -> Vector:
        x_point = endp[0] - start[0]
        y_point = endp[1] - start[1]
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self.x * other.x + self.y * other.y) / \
            (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)  # Positive Y axis
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, value: float) -> Vector:
        if isinstance(value, (int, float)):
            return Vector(self.x * value, self.y * value)
        elif isinstance(value, Vector):
            return self.x * value.x + self.y * value.y


# # Examples of usage:
# vector1 = Vector(2, 4)
# vector2 = Vector(-1, 3)
# vector3 = vector1 + vector2
# print(isinstance(vector3, Vector))  # True
# print(vector3.x, vector3.y)  # 1 7

# vector1 = Vector(2, 4)
# vector2 = Vector(-1, 3)
# vector3 = vector1 - vector2
# print(isinstance(vector3, Vector))  # True
# print(vector3.x, vector3.y)  # 3 1
