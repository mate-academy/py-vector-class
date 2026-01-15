import math
from typing import Union


class Vector:

    def __init__(self, x_location: Union[int, float],
                 y_location: Union[int, float]) -> None:
        self.x = round(x_location, 2)
        self.y = round(y_location, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        result_x = round(self.x - other.x, 2)
        result_y = round(self.y - other.y, 2)
        return Vector(result_x, result_y)

    def __mul__(self, other: Union[float, int, "Vector"])\
            -> Union["Vector", float]:
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, float):
            result_x = round(self.x * other, 2)
            result_y = round(self.y * other, 2)
            return Vector(result_x, result_y)

        return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, second_vector: "Vector") -> int:
        self_len = self.get_length()
        second_len = second_vector.get_length()
        acos_values = self.__mul__(second_vector) / (self_len * second_len)
        acos = math.acos(acos_values)
        return math.ceil(math.degrees(acos))

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            return 0

        if self.x == 0 and self.y > 0:
            return 0

        if self.x > 0 and self.y == 0:
            return 0

        if self.x > 0 and self.y > 0:
            return int(math.degrees(math.atan2(self.y, self.x)))

        if self.x < 0 and self.y > 0:
            angle = int(math.degrees(math.atan2(self.x, self.y)))
            if angle < 0:
                return abs(angle)
            return angle

        if self.x < 0 and self.y < 0:
            angle = int(math.degrees(math.atan2(self.x, self.y)))
            if angle < 0:
                return abs(angle)
            return angle

    def rotate(self, angle: int) -> "Vector":
        ange_radians = math.radians(angle)
        cos_angle = math.cos(ange_radians)
        sin_angle = math.sin(ange_radians)
        rotated_x = self.x * cos_angle - self.y * sin_angle
        rotated_y = self.x * sin_angle + self.y * cos_angle
        return Vector(rotated_x, rotated_y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)
