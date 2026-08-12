import math


class Vector:
    def __init__(self, x_dot: int | float, y_dot: int | float) -> None:
        self.x = round(x_dot, 2)
        self.y = round(y_dot, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        if start == (0, 0):
            return Vector(end[0], end[1])
        if end == (0, 0):
            return Vector(start[0], start[1])
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        cos = ((self.x * other.x + self.y * other.y)
               / (self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float | int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float | int) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(self.x * cos - self.y * sin, self.x * sin + self.y * cos)
