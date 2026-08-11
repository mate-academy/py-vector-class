import math
from typing import Union


class Vector:
    def __init__(self, x_cords: float, y_cords: float) -> None:
        self.x = round(x_cords, 2)
        self.y = round(y_cords, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[int, float, "Vector"]) \
            -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float],
            end_point: tuple[float, float]) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    @staticmethod
    def _to_degrees_and_round(radians: float) -> int:
        return round(math.degrees(radians))

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        lengths = self.get_length() * other.get_length()
        if lengths == 0:
            return 0
        cos_a = dot / lengths
        cos_a = max(-1.0, min(1.0, cos_a))
        return self._to_degrees_and_round(math.acos(cos_a))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        cos_a = self.y / length
        cos_a = max(-1.0, min(1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees_angle: float) -> "Vector":
        rad = math.radians(degrees_angle)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
