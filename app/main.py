import math
from typing import Union


class Vector:
    def __init__(self, variable_x: float, variable_y: float) -> None:
        self.x = round(variable_x, 2)
        self.y = round(variable_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float, int]) \
            -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 15)
        elif isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Vector' "
                            f"and '{type(other).__name__}'")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> "Vector":
        variable_x = round(end_point[0] - start_point[0], 2)
        variable_y = round(end_point[1] - start_point[1], 2)
        return cls(variable_x, variable_y)

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 15)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_mult = self.get_length() * other.get_length()
        if lengths_mult == 0:
            return 0
        cos_a = max(-1, min(1, dot_product / lengths_mult))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            return 0
        if self.x == 0:
            return 0 if self.y > 0 else 180
        angle = math.degrees(math.atan2(self.y, self.x))
        if angle < 0:
            angle += 360
        if 90 < angle < 180:
            angle -= 90
        elif 180 < angle < 270:
            angle -= 90
        return int(round(angle))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
