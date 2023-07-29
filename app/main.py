import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector') -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> 'Vector':
        x_coord = round(end_point[0] - start_point[0], 2)
        y_coord = round(end_point[1] - start_point[1], 2)
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> 'Vector':
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: 'Vector') -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        angle_radians = math.acos(cos_a)
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> 'Vector':
        angle_radians = math.radians(degrees)
        cos_a = math.cos(angle_radians)
        sin_a = math.sin(angle_radians)
        x_coord = self.x * cos_a - self.y * sin_a
        y_coord = self.x * sin_a + self.y * cos_a
        return Vector(round(x_coord, 2), round(y_coord, 2))
