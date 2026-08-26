from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x_coordinate = round(x_coordinate, 2)
        self.y_coordinate = round(y_coordinate, 2)

    @property
    def x(self) -> float:
        return self.x_coordinate

    @property
    def y(self) -> float:
        return self.y_coordinate

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            (self.x_coordinate + other.x_coordinate),
            (self.y_coordinate + other.y_coordinate)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            (self.x_coordinate - other.x_coordinate),
            (self.y_coordinate - other.y_coordinate)
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x_coordinate * other.x_coordinate
                    + self.y_coordinate * other.y_coordinate)

        if isinstance(other, (int, float)):
            return Vector(self.x_coordinate * other, self.y_coordinate * other)

        else:
            return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(
            self.x_coordinate ** 2 + self.y_coordinate ** 2
        )

    def get_normalized(self) -> Vector:
        return Vector(self.x_coordinate / self.get_length(),
                      self.y_coordinate / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(-self.x_coordinate, self.y_coordinate))
        if angle < 0:
            angle += 360
        return round(angle)

    def rotate(self, angle: float) -> Vector:
        radians_angle = math.radians(angle)
        rotated_x = (self.x_coordinate * math.cos(radians_angle)
                     - self.y_coordinate * math.sin(radians_angle))
        rotated_y = (self.x_coordinate * math.sin(radians_angle)
                     + self.y_coordinate * math.cos(radians_angle))

        return Vector(rotated_x, rotated_y)
