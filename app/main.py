import math


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> "Vector":
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(
            x=end_point[0] - start_point[0], y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector2: "Vector") -> float:
        scalar = self.x * vector2.x + self.y * vector2.y
        len1 = self.get_length()
        len2 = vector2.get_length()
        cos_angle = scalar / (len1 * len2)
        angle = math.degrees(math.acos(cos_angle))
        return math.ceil(angle)

    def get_angle(self) -> float:
        length = self.get_length()
        angle = math.degrees(math.acos(self.y / length))
        return round(angle)

    def rotate(self, degree: int) -> "Vector":
        radians = math.radians(degree)
        x1 = self.x * math.cos(radians) - self.y * math.sin(radians)
        y1 = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x1, y1)
