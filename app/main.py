from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.coordinate_x = round(coordinate_x, 2)
        self.coordinate_y = round(coordinate_y, 2)

    @property
    def x(self) -> float:
        return self.coordinate_x

    @property
    def y(self) -> float:
        return self.coordinate_y

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Unsupported addition type.")
        return Vector(self.coordinate_x + other.coordinate_x,
                      self.coordinate_y + other.coordinate_y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Unsupported subtraction type.")
        return Vector(self.coordinate_x - other.coordinate_x,
                      self.coordinate_y - other.coordinate_y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.coordinate_x * other, self.coordinate_y * other)
        if isinstance(other, Vector):
            return (self.coordinate_x * other.coordinate_x
                    + self.coordinate_y * other.coordinate_y)
        raise TypeError("Unsupported multiplication type.")

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.coordinate_x ** 2 + self.coordinate_y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.coordinate_x / length, self.coordinate_y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        cos_angle = self.coordinate_y / self.get_length()
        return round(math.degrees(math.acos(cos_angle)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.coordinate_x * math.cos(radians)
                 - self.coordinate_y * math.sin(radians))
        new_y = (self.coordinate_x * math.sin(radians)
                 + self.coordinate_y * math.cos(radians))
        return Vector(new_x, new_y)

    def __repr__(self) -> str:
        return f"Vector({self.coordinate_x}, {self.coordinate_y})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (round(self.coordinate_x, 2)
                == round(other.coordinate_x, 2)
                and round(self.coordinate_y, 2)
                == round(other.coordinate_y, 2))
