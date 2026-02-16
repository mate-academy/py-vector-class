import math
from typing import Union


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, int, "Vector"]) -> (
            Union)[float, int, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        dot = self.x * other.x + self.y * other.y
        len1 = self.get_length()
        len2 = other.get_length()
        cos = dot / (len1 * len2)
        cos = max(min(cos, 1), -1)
        angle = math.degrees(math.acos(cos))
        return int(round(angle))

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x, self.y))
        if angle < 0:
            angle += 360
        angle = (360 - angle) % 360
        return int(round(angle))

    def rotate(self, angle: int) -> "Vector":
        angle = math.radians(angle)
        old_x = self.x
        old_y = self.y
        new_x = old_x * math.cos(angle) - old_y * math.sin(angle)
        new_y = old_x * math.sin(angle) + old_y * math.cos(angle)
        return Vector(round(new_x, 2), round(new_y, 2))
