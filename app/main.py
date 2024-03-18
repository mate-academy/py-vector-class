import math
from typing import Tuple, Union


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x: float = round(x_coordinate, 2)
        self.y: float = round(y_coordinate, 2)

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[
                                        float, float]) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product: float = self * other
        self_length: float = self.get_length()
        other_length: float = other.get_length()
        cosine: float = dot_product / (self_length * other_length)
        angle: float = math.degrees(math.acos(cosine))
        return round(angle)

    def get_angle(self) -> int:
        y_axis: "Vector" = Vector(0, abs(self.y))
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians: float = math.radians(degrees)
        new_x: float = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y: float = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(
                "Multiplication is only supported with Vector or scalar "
                "(float, int) operands.")

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"
