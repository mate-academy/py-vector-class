import math


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | int | float") -> "Vector | float":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        x = round(end_point[0] - start_point[0], 2)
        y = round(end_point[1] - start_point[1], 2)
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            raise ValueError("cant normalized zero :(")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> float:
        scalar = float(self * other)
        length_multiple = float(self.get_length() * other.get_length())
        if length_multiple == 0:
            return 0.0
        cos_theta = float(scalar / length_multiple)
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def get_angle(self):
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot determine for zero vector")
        angle = math.degrees(math.acos(self.y / length))
        return round(angle)

    def rotate(self, degrees):
        radians = math.radians(degrees)
        x1 = self.x * math.cos(radians) - self.y * math.sin(radians)
        y1 = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x1, 2), round(y1, 2))
