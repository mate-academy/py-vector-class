import math
from typing import Union


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self,
                other: Union
                ["Vector", int, float]
                ) -> Union[float, "Vector"]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        return round((math.acos((self * other)
                                / ((self.get_length())
                                   * (other.get_length()))))
                     * (180 / math.pi))

    def get_angle(self) -> float:
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, angle):
        return Vector((self.x * math.cos(math.radians(angle)))
                      - (self.y * math.sin(math.radians(angle))),
                      (self.x * math.sin(math.radians(angle)))
                      + (self.y * math.cos(math.radians(angle))))
