from __future__ import annotations
import math


class Vector:
    def __init__(self, x_val: int | float, y_val: int | float) -> None:
        self.x = round(x_val, 2)
        self.y = round(y_val, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_val=self.x + other.x, y_val=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_val=self.x - other.x, y_val=self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_val=self.x * other, y_val=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[int | float],
                                    end_point: tuple[int | float]
                                    ) -> Vector:
        return Vector(
            x_val=end_point[0] - start_point[0],
            y_val=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        coefficient = self.get_length()
        return Vector(x_val=self.x / coefficient, y_val=self.y / coefficient)

    def angle_between(self, other: Vector) -> int :
        return round(math.degrees(math.acos((self * other)
                                            / (self.get_length()
                                            * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x_val=self.x * math.cos(radians) - self.y * math.sin(radians),
            y_val=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
