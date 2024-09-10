import math
from typing import Union, Tuple


class Vector:
    def __init__(
            self,
            x_axis: Union[int, float],
            y_axis: Union[int, float]
    ) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(
            self,
            other: Union[int, float, "Vector"]
    ) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: Tuple[Union[int, float], Union[int, float]],
            end_point: Tuple[Union[int, float], Union[int, float]]
    ) -> "Vector":
        x_axis = round(end_point[0] - start_point[0], 2)
        y_axis = round(end_point[1] - start_point[1], 2)
        return cls(x_axis, y_axis)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> float:
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()
        cos_angle = dot_product / (length_self * length_other)
        cos_angle = max(-1, min(1, cos_angle))
        angle_in_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(round(new_x, 2), round(new_y, 2))


if __name__ == "__main__":
    vector1 = Vector(13, -4)
    vector2 = Vector(-6, -11)
    print(vector1.angle_between(vector2))
