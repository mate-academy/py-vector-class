from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector | ValueError:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return ValueError("Not a Vector")

    def __sub__(self, other: Vector) -> Vector | ValueError:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return ValueError("Not a Vector")

    def __mul__(self, other: int | float | Vector) \
            -> Vector | float | ValueError:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return ValueError("Not a Vector or float number")

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector | ValueError:
        if (isinstance(start_point, tuple)
                and isinstance(end_point, tuple)):
            return Vector(end_point[0] - start_point[0],
                          end_point[1] - start_point[1])
        return ValueError("Not a Vector")

    def get_length(self) -> float | ValueError:
        if isinstance(self, Vector):
            return (self.x ** 2 + self.y ** 2) ** 0.5
        return ValueError("Not a Vector")

    def get_normalized(self) -> Vector | ValueError:
        if isinstance(self, Vector):

            length = self.get_length()
            return Vector(self.x / length, self.y / length)
        return ValueError("Not a Vector")

    def angle_between(self, other: Vector) -> float | ValueError:
        if isinstance(self, Vector) and isinstance(other, Vector):
            cos_a = (self.__mul__(other)
                     / (self.get_length() * other.get_length()))
            return round(math.degrees(math.acos(cos_a)))
        return ValueError("Not a Vector")

    def get_angle(self) -> float | ValueError:
        if isinstance(self, Vector):
            return round(math.degrees(math.acos
                                      (self.y / self.get_length())))
        return ValueError("Not a Vector")

    def rotate(self, angle: int) -> Vector | ValueError:
        if isinstance(angle, int):
            # x' = x·cos θ - y·sin θ, y' = x·sin θ + y·cos θ
            pi_value = math.pi
            angle_radians = angle * (pi_value / 180)
            return Vector(self.x * math.cos(angle_radians)
                          - self.y * math.sin(angle_radians),
                          self.x * math.sin(angle_radians)
                          + self.y * math.cos(angle_radians))
        return ValueError("Not a Vector")
