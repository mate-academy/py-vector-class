from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        raise TypeError("Unsupported operand type(s)")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        raise TypeError("Unsupported operand type(s)")

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, (float, int)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                "Unsupported operand type(s) for *: "
                "'Vector' and '{}".format(type(other))
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:

        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return (
            round
            (
                math.degrees(
                    math.acos(
                        self * other / (
                            self.get_length() * other.get_length()
                        )
                    )
                )
            )
        )

    def get_angle(self) -> int:
        j_vector = Vector(0, 1)
        return self.angle_between(other=j_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
