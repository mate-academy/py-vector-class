import math

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: "Vector", end_point: "Vector") -> "Vector":
        if isinstance(start_point, Vector) and isinstance(end_point, Vector):
            return cls(end_point.x - start_point.x, end_point.y - start_point.y)


    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = self.x / length if length != 0 else 0
        normalized_y = self.y / length if length != 0 else 0
        return Vector(round(normalized_x, 1), round(normalized_y, 1))

    def angle_between(self, other: "Vector") -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        vector_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        vector_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(vector_x, vector_y)
