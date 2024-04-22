import math


class Vector:
    def __init__(self, x1: float, y1: float) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float or "Vector") -> "Vector" or float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        x1 = end[0] - start[0]
        y1 = end[1] - start[1]
        return cls(x1, y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        angle_in_radians = math.atan2(self.x, self.y)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(math.fabs(angle_in_degrees))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
