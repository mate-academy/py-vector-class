import math
from typing import Union


class Vector:
    def __init__(self, x_asix: float, y_asix: float) -> None:
        self.x = round(x_asix, 2)
        self.y = round(y_asix, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, int, "Vector"]) \
            -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"unsupported operand type(s) for *: "
                            f" {type(self)} and {type(other)}")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple
                                    [float, float], end_point:
                                    tuple[float, float]) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        scalar = self.x * other.x + self.y * other.y
        length = self.get_length() * other.get_length()
        cos_angle = scalar / length
        angle = round(math.degrees(math.acos(cos_angle)))
        return angle

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        angle = math.degrees(math.atan2(-self.x, self.y))
        if angle < 0:
            return int(round(angle + 360))
        return int(round(angle))

    def rotate(self, angle: float) -> "Vector":
        angle_rad = math.radians(angle)
        x_asix = (self.x * math
                  .cos(angle_rad) - self
                  .y * math.sin(angle_rad))
        y_asix = (self.x * math.
                  sin(angle_rad)
                  + self.y
                  * math.cos(angle_rad))
        return Vector(round(x_asix, 2), round(y_asix, 2))

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
