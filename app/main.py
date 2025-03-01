import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector | int | float") -> "Vector | int | float":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return Vector(self.x + other, self.y + other)

    def __sub__(self, other: "Vector | int | float") -> "Vector | int | float":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return Vector(self.x - other, self.y - other)

    def __mul__(self, other: "Vector | int | float") -> "Vector | int|  float":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        length_self = self.get_length()
        length_vector = vector.get_length()

        if length_self == 0 or length_vector == 0:
            return 0

        cos_theta = dot_product / (length_self * length_vector)
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def get_angle(self) -> int:
        if self.x == 0 and self.y == 0:
            return 0

        angle = math.degrees(math.atan2(-self.x, self.y))

        if angle < 0:
            angle += 360
        return round(angle)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        x_new = round(self.x * math.cos(radians) /
                      - self.y * math.sin(radians), 2)
        y_new = round(self.x * math.sin(radians) /
                      + self.y * math.cos(radians), 2)
        return Vector(x_new, y_new)

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
