import math
from typing import Union, Tuple


class Vector:
    def __init__(
            self, x_value: Union[int, float], y_value: Union[int, float]
    ) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, point: "Vector") -> "Vector":
        return Vector(self.x + point.x, self.y + point.y)

    def __sub__(self, point: "Vector") -> "Vector":
        return Vector(self.x - point.x, self.y - point.y)

    def __mul__(
            self,
            number: Union[int, float, "Vector"]
    ) -> Union["Vector", float]:
        if isinstance(number, (int, float)):
            return Vector(round(self.x * number, 2), round(self.y * number, 2))
        elif isinstance(number, Vector):
            return self.x * number.x + self.y * number.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: Tuple[Union[int, float], Union[int, float]],
        end_point: Tuple[Union[int, float], Union[int, float]]
    ) -> "Vector":
        x_number = end_point[0] - start_point[0]
        y_number = end_point[1] - start_point[1]
        return cls(x_number, y_number)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        if self.get_length() != 0:
            return Vector(
                round(self.x / self.get_length(), 2),
                round(self.y / self.get_length(), 2)
            )

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1, min(1, cos_theta))
        angle_degrees = math.degrees(math.acos(cos_theta))
        return round(angle_degrees)

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.x, self.y))
        return abs(round(angle))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
