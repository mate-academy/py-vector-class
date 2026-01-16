import math


class Vector:
    def __init__(self, x1: float, y1: float) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(x1=self.x + other.x, y1=self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(x1=self.x - other.x, y1=self.y - other.y)

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x1=self.x * other, y1=self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float], end_point: tuple[float]
    ) -> "Vector":
        return cls(
            x1=end_point[0] - start_point[0], y1=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (pow(self.x, 2) + pow(self.y, 2)) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(x1=self.x / length, y1=self.y / length)

    def angle_between(self, other: "Vector") -> int:
        mul = self.__mul__(other)
        mul_length = self.get_length() * other.get_length()
        cos_angle = mul / mul_length
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        return math.trunc(math.degrees(math.acos(cos_angle)))

    def rotate(self, angle: int) -> "Vector":
        radian = math.radians(angle)
        x2 = math.cos(radian) * self.x - math.sin(radian) * self.y
        y2 = math.sin(radian) * self.x + math.cos(radian) * self.y
        return Vector(x1=x2, y1=y2)
