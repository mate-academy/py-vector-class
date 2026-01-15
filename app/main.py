import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: object) -> object:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: object) -> object:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            vector_a = [self.x, self.y]
            vector_b = [other.x, other.y]
            dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
            return dot_product

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_pont: tuple) -> object:
        return cls(
            end_pont[0] - start_point[0],
            end_pont[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        magnitude = self.get_length()
        return Vector(
            self.x / magnitude,
            self.y / magnitude
        )

    def angle_between(self, other: object) -> int:
        vector_a = [self.x, self.y]
        vector_b = [other.x, other.y]
        dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
        magnitude_1 = self.get_length()
        magnitude_2 = other.get_length()
        angle_radians = math.acos(dot_product / (magnitude_1 * magnitude_2))
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees)

    def get_angle(self) -> int:
        other = Vector(0, 10)

        return self.angle_between(other)

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        return Vector(
            cos_theta * self.x - sin_theta * self.y,
            sin_theta * self.x + cos_theta * self.y
        )
