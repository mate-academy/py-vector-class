import math
from typing import Union


class Vector:
    def __init__(self, cord_x: float | int, cord_y: float | int) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float]
                ) -> Union["Vector", float, int]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1]
                   )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int | float:
        return round(math.degrees(math.acos((self * other)
                                            / (self.get_length()
                                            * other.get_length()))))

    def get_angle(self) -> int | float:
        return round(math.degrees(math.acos((self.y * 1) / self.get_length())))

    def rotate(self, other: int | float) -> "Vector":
        angle = math.radians(other)
        return Vector(round(math.cos(angle) * self.x
                            - math.sin(angle) * self.y, 2),
                      round(math.sin(angle) * self.x
                            + math.cos(angle) * self.y, 2)
                      )
