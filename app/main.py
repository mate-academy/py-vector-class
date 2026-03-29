import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        x = abs(self.x)
        y = abs(self.y)
        return math.sqrt(x * x + y * y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        numerator = self * other
        denominator = self.get_length() * other.get_length()
        return int(math.acos(numerator / denominator))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, dig: int) -> Vector:
        x2 = self.x * math.cos(dig) - self.y * math.sin(dig)
        y2 = self.x * math.sin(dig) + self.y * math.cos(dig)
        return Vector(x2, y2)
