from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y
                      + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y
                      - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            dot_product = (self.x * other.x + self.y
                           * other.y)
            return dot_product
        else:
            raise TypeError(f"Unsupported operation for * with type "
                            f"{type(other)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with a "
                             "zero-length vector.")
        cos_angle = max(min(dot_product / lengths_product, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float:
        reference = Vector(0, 1)
        return self.angle_between(reference)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = (self.x * math.cos(radians) - self.y
                 * math.sin(radians))
        new_y = (self.x * math.sin(radians) + self.y
                 * math.cos(radians))
        return Vector(new_x, new_y)
