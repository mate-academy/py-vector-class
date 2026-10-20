import math


class Vector:
    def __init__(self, coordinate_x: float | int, coordinate_y: float | int
                 ) -> None:
        self.x = round(float(coordinate_x), 2)
        self.y = round(float(coordinate_y), 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float
                ) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        new_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        new_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(new_x, new_y)
