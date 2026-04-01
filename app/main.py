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

    def __mul__(self,
                other: Union[float, int, "Vector"]) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        cos_of_angle = ((self * other)
                        / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_of_angle)))

    def get_angle(self) -> int:
        cos_of_angle = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_of_angle)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        return Vector(self.x * math.cos(radians) - self.y * math.sin(radians),
                      self.y * math.cos(radians) + self.x * math.sin(radians))
