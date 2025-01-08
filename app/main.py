import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> float | "Vector":
        if isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 4)
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            return 0
        cos_angle = max(-1.0, min(1.0, dot_product / lengths_product))
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(round(new_x, 2), round(new_y, 2))
