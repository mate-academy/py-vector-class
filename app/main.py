import math


class Vector:
    # write your code here
    def __init__(self, x, y) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        x1, y1 = start
        x2, y2 = end
        return Vector(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        x_2 = pow(self.x, 2)
        y_2 = pow(self.y, 2)
        return math.sqrt(x_2 + y_2)

    def get_normalized(self) -> "Vector":
        magnitude = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        first_div = round(self.x / abs(magnitude), 2)
        second_div = round(self.y / abs(magnitude), 2)
        return Vector(first_div, second_div)

    def angle_between(self, other: Vector) -> float:
        mul_vectors = self.x * other.x + self.y * other.y
        two_abs = math.sqrt(pow(self.x, 2) + pow(self.y, 2)) * math.sqrt(
            pow(other.x, 2) + pow(other.y, 2)
        )
        angle = round(math.degrees(math.acos(mul_vectors / two_abs)))
        return angle

    def get_angle(self) -> float:
        magnitude = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        if magnitude == 0:
            return 0.0
        angle = round(math.degrees(math.acos(self.y / magnitude)))
        return angle

    def rotate(self, rotation_degr: int) -> "Vector":
        x_prime = self.x * math.cos(
            math.radians(rotation_degr)
        ) - self.y * math.sin(math.radians(rotation_degr))
        y_prime = self.x * math.sin(
            math.radians(rotation_degr)
        ) + self.y * math.cos(math.radians(rotation_degr))
        return Vector(x_prime, y_prime)
