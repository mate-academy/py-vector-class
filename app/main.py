import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x: float = round(x, 2)
        self.y: float = round(y, 2)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> float or 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector') -> float or 'Vector':
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> 'Vector':
        x = round(end_point[0] - start_point[0], 2)
        y = round(end_point[1] - start_point[1], 2)
        return cls(x, y)

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
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> float or 'Vector':
        angle_radians = math.radians(degrees)
        cos_a = math.cos(angle_radians)
        sin_a = math.sin(angle_radians)
        x = self.x * cos_a - self.y * sin_a
        y = self.x * sin_a + self.y * cos_a
        return Vector(round(x, 2), round(y, 2))
