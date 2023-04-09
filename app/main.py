import math
from typing import Union


class Vector:
    def __init__(self, ex: float, ey: float) -> None:
        self.x = round(ex, 2)
        self.y = round(ey, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, "Vector"]) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float,
                                    float]) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> float:
        dot_product = self.x * other.x + self.y * other.y
        self_length = math.sqrt(self.x ** 2 + self.y ** 2)
        other_length = math.sqrt(other.x ** 2 + other.y ** 2)
        angle_radians = math.acos(dot_product / (self_length * other_length))
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees, 0)

    def get_angle(self) -> float:
        y_axis_vector = Vector(0, 1)
        return self.angle_between(y_axis_vector)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = round((math.cos(radians) * self.x
                       - math.sin(radians) * self.y), 2)
        new_y = round((math.sin(radians) * self.x
                       + math.cos(radians) * self.y), 2)
        return Vector(new_x, new_y)
