import math
from typing import Union


class Vector:
    def __init__(self, x_coord: (float, int), y_coord: (float, int)) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: (float,
                              int,
                              "Vector")) -> Union["Vector", int, float]:
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> Union[int, float]:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_of_angle = (self * other) / (self.get_length()
                                         * other.get_length())
        return round(math.degrees(math.acos(cos_of_angle)))

    def get_angle(self) -> int:
        y_vector = Vector(0, 1)
        return self.angle_between(y_vector)

    def rotate(self, degrees: int) -> "Vector":
        angle_radians = math.radians(degrees)
        new_x = (self.x * math.cos(angle_radians) - self.y
                 * math.sin(angle_radians))
        new_y = (self.x * math.sin(angle_radians) + self.y
                 * math.cos(angle_radians))
        return Vector(new_x, new_y)
