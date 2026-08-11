import math


class Vector:

    def __init__(
            self,
            coordinate_x: int | float,
            coordinate_y: int | float) \
            -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) \
            -> Vector:
        coordinate_x = end_point[0] - start_point[0]
        coordinate_y = end_point[1] - start_point[1]

        return cls(coordinate_x, coordinate_y)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        coordinate_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        coordinate_y = math.sin(radians) * self.x + math.cos(radians) * self.y

        return Vector(coordinate_x, coordinate_y)
