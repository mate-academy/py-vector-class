import math
from typing import Tuple, Union


class Vector:
    def __init__(self, coord_x: Union[int, float],
                 coord_y: Union[int, float]) -> None:
        self.x: float = round(coord_x, 2)
        self.y: float = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Union[int, float, "Vector"]) \
            -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        elif isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        else:
            raise TypeError

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]
                                    ) -> "Vector":
        x1, y1 = start_point
        x2, y2 = end_point
        new_x = x2 - x1
        new_y = y2 - y1
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product = self * other_vector
        lengths_product = self.get_length() * other_vector.get_length()
        if lengths_product == 0:
            return 0
        cos_a = dot_product / lengths_product
        cos_a = max(-1.0, min(1.0, cos_a))
        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def get_angle(self) -> int:
        angle_deg_x = math.degrees(math.atan2(self.y, self.x))
        angle_deg_x = (angle_deg_x + 360) % 360
        angle_deg_y = angle_deg_x - 90
        angle_deg_y = (angle_deg_y + 360) % 360
        return int(round(angle_deg_y))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        current_x = self.x
        current_y = self.y
        new_x = current_x * math.cos(radians) - current_y * math.sin(radians)
        new_y = current_x * math.sin(radians) + current_y * math.cos(radians)
        return Vector(new_x, new_y)
