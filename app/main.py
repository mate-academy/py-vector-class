import math
from math import degrees, acos, sin, cos, radians


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        v1 = self.x + other.x
        v2 = self.y + other.y
        return Vector(v1, v2)

    def __sub__(self, other: Vector) -> Vector:
        v1 = self.x - other.x
        v2 = self.y - other.y
        return Vector(v1, v2)

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, Vector):
            v1 = self.x * other.x
            v2 = self.y * other.y
            dot_product = v1 + v2
            return dot_product
        else:
            v1 = self.x * other
            v2 = self.y * other
            return Vector(v1, v2)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple,
    ) -> Vector:
        v1 = end_point[0] - start_point[0]
        v2 = end_point[1] - start_point[1]
        return cls(v1, v2)

    def get_length(self) -> float:
        v1 = self.x ** 2
        v2 = self.y ** 2
        return (v1 + v2) ** 0.5

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            raise ValueError("Cannot normalize zero-length vector")
        v1 = self.x / self.get_length()
        v2 = self.y / self.get_length()
        return Vector(v1, v2)

    def angle_between(self, other: Vector) -> int:
        part1 = self.x * other.x + self.y * other.y
        part2 = self.get_length() * other.get_length()
        answer = math.degrees(math.acos(part1 / part2))
        return int((answer + 0.5) // 1)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        part1 = self.y / length
        part2 = degrees(acos(part1))
        return int(part2)

    def rotate(self, number: int) -> Vector:
        part1 = self.x * cos(radians(number)) - self.y * sin(radians(number))
        part2 = self.x * sin(radians(number)) + self.y * cos(radians(number))
        return Vector(part1, part2)
