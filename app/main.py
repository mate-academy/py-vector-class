import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError

    def __mul__(self, other: "int | float | Vector") -> "Vector | int | float":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        raise TypeError

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot get normalized vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot = self * other
        length = self.get_length() * other.get_length()
        cos_a = dot / length

        cos_a = max(-1, min(1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
