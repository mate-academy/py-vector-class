import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    @property
    def x(self) -> float:
        return self.x_coord

    @property
    def y(self) -> float:
        return self.y_coord

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coord + other.x_coord,
                      self.y_coord + other.y_coord)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_coord - other.x_coord,
                      self.y_coord - other.y_coord)

    def __mul__(self, other: Union[int, float, "Vector"])\
            -> Union["Vector", float]:
        if isinstance(other, (float, int)):
            return Vector(self.x_coord * other,
                          self.y_coord * other)
        else:
            return ((self.x_coord * other.x_coord)
                    + (self.y_coord * other.y_coord))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x_coord**2 + self.y_coord**2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x_coord / self.get_length(),
                      self.y_coord / self.get_length())

    def angle_between(self, vector: "Vector") -> int:
        cos_a = ((self.x_coord * vector.x_coord
                  + self.y_coord * vector.y_coord)
                 / (self.get_length() * vector.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x_coord, self.y_coord))))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_cord = (self.x_coord * math.cos(radians)
                  - self.y_coord * math.sin(radians))
        y_cord = (self.x_coord * math.sin(radians)
                  + self.y_coord * math.cos(radians))
        return Vector(x_cord, y_cord)
