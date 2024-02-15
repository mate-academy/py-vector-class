import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: object) -> object:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: object) -> object:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: object | int | float) -> object | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> object:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length(),
        )

    def angle_between(self, other: object) -> int:
        len_a = self.get_length()
        len_b = other.get_length()
        len_c = ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        result = (len_a ** 2 + len_b ** 2 - len_c ** 2) / (2 * len_a * len_b)
        return round(math.degrees(math.acos(result)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> object:
        radians = math.radians(angle)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
