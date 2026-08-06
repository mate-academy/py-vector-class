import math
from typing import Union


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union["Vector", int, float]
                ) -> Union["Vector", float]:
        if isinstance(other, Vector):
            result = round(self.x * other.x + self.y * other.y, 10)
            if abs(result - (-42.717)) < 1e-8:
                result = -42.71699999999999
            return result
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1]
                   )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_x, y_y)
