import math


class Vector:
    def __init__(self, x: int, y: int):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # dot product
        else:
            raise TypeError("Unsupported operand type for *: {}".format(type(other)))

    @classmethod

    def create_vector_by_two_points(cls, start_point, end_point) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])
    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: float) -> None:
        product = self * other
        cos_angle = product / (self.get_length() * other.get_length())
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)

    def get_angle(self) -> "Vector":
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
