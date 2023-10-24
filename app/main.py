from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: (int, float), point_y: (int, float)) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: (int, float, Vector)) -> (Vector, int):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            (end_point[0] - start_point[0]),
            (end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length > 0:
            return Vector((self.x / length), (self.y / length))
        return Vector(0, 0)

    def angle_between(self, vector: Vector) -> int:
        cosine = self.__mul__(vector)\
            / (self.get_length()
                * vector.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_point_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_point_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_point_x, new_point_y)
