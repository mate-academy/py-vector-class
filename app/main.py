import math
from typing import Tuple, Union


class Vector:
    def __init__(self, _x: float, _y: float) -> None:
        self.x: float = round(_x, 2)
        self.y: float = round(_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"])\
            -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise ValueError(f"Multiplication with type "
                         f"{type(other)} is not supported")

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) \
            -> "Vector":
        x_ = end_point[0] - start_point[0]
        y_ = end_point[1] - start_point[1]
        return cls(x_, y_)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with zero vector")
        cos_angle = max(-1.0, min(1.0, dot_product
                                  / lengths_product))  # Clamp to [-1, 1]
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)  # Positive Y axis
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
