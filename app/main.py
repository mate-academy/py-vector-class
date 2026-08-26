from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float | int, vector_y: float | int) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y}"

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        elif isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        else:
            raise TypeError(f"cant operant *: with {self} and {other}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:

        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        if vector_length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(
            self.x / vector_length,
            self.y / vector_length
        )

    def angle_between(self, another_vector: Vector) -> float:
        dot_product = self * another_vector
        len_vector1 = self.get_length()
        len_vector2 = another_vector.get_length()
        cos_theta = dot_product / (len_vector1 * len_vector2)
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> float:
        cos_theta = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        return Vector(
            round(self.x * cos_theta - self.y * sin_theta, 2),
            round(self.x * sin_theta + self.y * cos_theta, 2)
        )


vector = Vector(33, 8)
vector2 = vector.rotate(45)

print(vector2.x)  # == 17.68
print(vector2.y)  # == 28.99
