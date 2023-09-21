import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: object) -> object:
        return Vector(
            self.x + vector.x,
            self.y + vector.y
        )

    def __sub__(self, vector: object) -> object:
        return Vector(
            self.x - vector.x,
            self.y - vector.y
        )

    def __mul__(self, multiplier: object | float) -> object | float:
        if isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y
        return Vector(
            self.x * multiplier,
            self.y * multiplier
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> object:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> object:
        return Vector(
            self.x * (1 / Vector.get_length(self)),
            self.y * (1 / Vector.get_length(self))
        )

    def angle_between(self, other: object) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            self.x * cos - self.y * sin,
            self.x * sin + self.y * cos
        )

