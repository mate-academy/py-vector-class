# noqa: flake8-variable-names
import math


class Vector:
    # write your code here
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: float) -> float:
        return Vector(
            self.x + other.x, self.y + other.y
        )

    def __sub__(self, other: float) -> float:
        return Vector(
            self.x - other.x, self.y - other.y
        )

    def __mul__(self, other: float) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: float, end_point: float
    ) -> float:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> float:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: float) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> float:
        radians = math.radians(degrees)
        new_x = \
            self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = \
            self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
