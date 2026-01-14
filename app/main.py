import math
from typing import Union


class Vector:

    def __init__(self, _x: float, _y: float) -> None:
        self._x = round(_x, 2)
        self._y = round(_y, 2)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self._x + other.x
        new_y = self._y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self._x - other.x
        new_y = self._y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Union[int, float, "Vector"])\
            -> Union[int, float, "Vector"]:
        if isinstance(other, Vector):
            dot_point = self._x * other.x + self._y * other.y
            return dot_point
        else:
            new_x = self._x * other
            new_y = self._y * other
        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> "Vector":
        x1 = start_point[0]
        y1 = start_point[1]
        x2 = end_point[0]
        y2 = end_point[1]
        new_x = x2 - x1
        new_y = y2 - y1
        return cls(new_x, new_y)

    def get_length(self) -> float:
        length_result = (self._x ** 2 + self._y ** 2) ** 0.5
        return length_result

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        normalized_x = self._x / length
        normalized_y = self._y / length
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self._x * other.x + self._y * other.y
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_theta = dot_product / length_product
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> float:
        length = self.get_length()
        if length == 0:
            return 0
        cos_theta = self._y / length
        cos_theta = max(-1.0, min(1.0, cos_theta))
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        if self._x < 0:
            pass
        return round(angle_deg)

    def rotate(self, degrees: float) -> "Vector":
        angle_rad = math.radians(degrees)
        cos_phi = math.cos(angle_rad)
        sin_phi = math.sin(angle_rad)
        new_x = self._x * cos_phi - self._y * sin_phi
        new_y = self._x * sin_phi + self._y * cos_phi
        return Vector(new_x, new_y)
