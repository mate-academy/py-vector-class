from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_coord=(self.x + other.x), y_coord=(self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_coord=(self.x - other.x), y_coord=(self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                x_coord=round((self.x * other), 2),
                y_coord=round((self.y * other), 2)
            )
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_coord=(end_point[0] - start_point[0]),
            y_coord=(end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        return math.sqrt(
            (math.pow(abs(self.x), 2)) + (math.pow(abs(self.y), 2))
        )

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x_coord=self.x / length, y_coord=self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = (self.x * other.x) + (self.y * other.y)
        magnitude_of_vectors_product = \
            math.sqrt((math.pow(self.x, 2)) + (math.pow(self.y, 2))) \
            * math.sqrt((math.pow(other.x, 2)) + (math.pow(other.y, 2)))
        cosine_of_angle = dot_product / magnitude_of_vectors_product
        return round(math.degrees(math.acos(cosine_of_angle)))

    def get_angle(self) -> int:
        result = (self.y / math.sqrt((math.pow(self.x, 2))
                                     + (math.pow(self.y, 2))))
        return round(math.degrees(math.acos(result)))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            x_coord=(self.x * math.cos(degrees) - self.y * math.sin(degrees)),
            y_coord=(self.x * math.sin(degrees) + self.y * math.cos(degrees))
        )
