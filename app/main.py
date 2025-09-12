import math
from typing import Tuple, Union


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x: float = round(coordinate_x, 2)
        self.y: float = round(coordinate_y, 2)

    def __add__(self, other_vector: "Vector") -> "Vector":
        new_x: float = self.x + other_vector.x
        new_y: float = self.y + other_vector.y
        return Vector(new_x, new_y)

    def __sub__(self, other_vector: "Vector") -> "Vector":
        new_x: float = self.x - other_vector.x
        new_y: float = self.y - other_vector.y
        return Vector(new_x, new_y)

    def __mul__(
        self, other: Union["Vector", float]
    ) -> Union["Vector", float]:
        if isinstance(other, Vector):
            dot_product: float = (
                self.x * other.x + self.y * other.y
            )
            return round(dot_product, 4)
        else:
            new_x: float = self.x * other
            new_y: float = self.y * other
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float],
        end_point: Tuple[float, float]
    ) -> "Vector":
        delta_x: float = end_point[0] - start_point[0]
        delta_y: float = end_point[1] - start_point[1]
        return cls(delta_x, delta_y)

    def get_length(self) -> float:
        length: float = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> "Vector":
        vector_length: float = self.get_length()
        if vector_length == 0:
            return Vector(0, 0)
        normalized_x: float = self.x / vector_length
        normalized_y: float = self.y / vector_length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product: float = self * other_vector
        self_length: float = self.get_length()
        other_length: float = other_vector.get_length()
        if self_length == 0 or other_length == 0:
            return 0
        cosine_of_angle: float = dot_product / (
            self_length * other_length
        )
        cosine_of_angle = max(min(cosine_of_angle, 1), -1)
        angle_in_degrees: float = math.degrees(
            math.acos(cosine_of_angle)
        )
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        angle_in_radians: float = math.atan2(self.x, self.y)
        angle_in_degrees: float = math.degrees(angle_in_radians)
        if angle_in_degrees < 0:
            angle_in_degrees += 360
        return round(angle_in_degrees)

    def rotate(self, degrees_to_rotate: int) -> "Vector":
        radians_to_rotate: float = math.radians(degrees_to_rotate)
        cosine: float = math.cos(radians_to_rotate)
        sine: float = math.sin(radians_to_rotate)
        rotated_x: float = (
            self.x * cosine - self.y * sine
        )
        rotated_y: float = (
            self.x * sine + self.y * cosine
        )
        return Vector(rotated_x, rotated_y)
