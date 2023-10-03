from typing import Any
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)    # problems with result???????????

    def __add__(self, other: Any) -> "Vector":    # need annotation
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other[0], self.y + other[1])

    def __sub__(self, other: Any) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other[0], self.y - other[1])

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_points: tuple,
                                    end_points: tuple) -> "Vector":
        return cls(end_points[0] - start_points[0],
                   end_points[1] - start_points[1])

    def get_length(self) -> float:
        return math.sqrt((pow(self.x, 2)) + (pow(self.y, 2)))

    def get_normalized(self) -> "Vector":
        length = math.sqrt((pow(self.x, 2)) + (pow(self.y, 2)))
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        upper_part = self * other
        footer_part = (math.sqrt((pow(self.x, 2)) + (pow(self.y, 2)))
                       * math.sqrt((pow(other.x, 2)) + (pow(other.y, 2))))
        arg_cos = upper_part / footer_part
        arg_cos_result = math.acos(arg_cos)
        arg_cos_result_degrees = math.degrees(arg_cos_result)
        return int(round(arg_cos_result_degrees, 0))

    def get_angle(self) -> int:
        vector1 = Vector(0, 1)
        upper_part = self * vector1
        footer_part = (math.sqrt((pow(self.x, 2)) + (pow(self.y, 2)))
                       * math.sqrt((pow(vector1.x, 2)) + (pow(vector1.y, 2))))
        arg_cos = upper_part / footer_part
        arg_cos_result = math.acos(arg_cos)
        arg_cos_result_degrees = math.degrees(arg_cos_result)
        return int(round(arg_cos_result_degrees, 0))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
