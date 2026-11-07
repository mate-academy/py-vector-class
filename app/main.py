import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        x_coord = end[0] - start[0]
        y_coord = end[1] - start[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        first_magnitude = self.get_length()
        second_magnitude = Vector.get_length(other)
        cos = dot_product / (first_magnitude * second_magnitude)
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_coord = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_coord = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_coord, y_coord)
