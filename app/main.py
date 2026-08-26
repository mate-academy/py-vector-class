import math


class Vector:

    def __init__(self, var1: float, var2: float) -> None:
        self.x = round(var1, 2)
        self.y = round(var2, 2)

    def __add__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: float,
                                    end_point: float) -> "Vector":
        var1 = end_point[0] - start_point[0]
        var2 = end_point[1] - start_point[1]
        return cls(var1, var2)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: float) -> float:
        dot_product = (self.x * other.x) + (self.y * other.y)
        magnitude1 = math.sqrt(self.x ** 2 + self.y ** 2)
        magnitude2 = math.sqrt(other.x ** 2 + other.y ** 2)
        magnitude = magnitude1 * magnitude2
        cos_a = dot_product / magnitude
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        dot_product = self.y
        magnitude1 = math.sqrt(self.x ** 2 + self.y ** 2)
        magnitude2 = 1
        magnitude = magnitude1 * magnitude2
        cos_a = dot_product / magnitude
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        var1 = self.x * math.cos(radians) - self.y * math.sin(radians)
        var2 = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(var1, 2), round(var2, 2))
