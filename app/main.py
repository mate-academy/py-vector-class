from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            coord_x: int | float,
            coord_y: int | float
    ) -> None:
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.coord_x + other.coord_x, 2),
            round(self.coord_y + other.coord_y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.coord_x - other.coord_x, 2),
            round(self.coord_y - other.coord_y, 2)
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.coord_x * other, 2),
                round(self.coord_y * other, 2)
            )
        return self.coord_x * other.coord_x + self.coord_y * other.coord_y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int, int],
            end_point: tuple[int, int]
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_normalized(self) -> Vector:
        vector_norm = math.sqrt(self.coord_x ** 2 + self.coord_y ** 2)
        return Vector(
            round(self.coord_x / vector_norm, 2),
            round(self.coord_y / vector_norm, 2)
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = (self.coord_x * other.coord_x
                       + self.coord_y * other.coord_y)
        magnitude = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(dot_product / magnitude)))

    def get_angle(self) -> int:
        dot_product = self.coord_x * 0 + self.coord_y * 1
        magnitude = (self.get_length()
                     * math.sqrt(0 ** 2 + 1 ** 2))
        return round(math.degrees(math.acos(dot_product / magnitude)))

    def rotate(self, degrees: int) -> Vector:
        coord_x = (self.coord_x * math.cos(math.radians(degrees))
                   - self.coord_y * math.sin(math.radians(degrees)))

        coord_y = (self.coord_x * math.sin(math.radians(degrees))
                   + self.coord_y * math.cos(math.radians(degrees)))

        return Vector(round(coord_x, 2), round(coord_y, 2))
