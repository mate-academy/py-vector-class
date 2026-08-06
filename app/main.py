import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other,
                          self.y * other)
        return (self.x * other.x + self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple):
        return cls(end[0] - start[0] , end[1] - start[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector):
        sum_of_two_vectors = self.x * vector.x + self.y * vector.y
        sqrt_vector1 = math.sqrt(self.x ** 2 + self.y ** 2)
        sqrt_vector2 = math.sqrt(vector.x ** 2 + vector.y ** 2)
        result = sum_of_two_vectors / (sqrt_vector2 * sqrt_vector1)
        return math.ceil(math.degrees(math.acos(result)))

    def get_angle(self):
        sqrt_of_a_vector = math.sqrt(self.x ** 2 + self.y ** 2)
        result = self.y / sqrt_of_a_vector
        return int(math.degrees(math.acos(result)))

    def rotate(self, degrees):
        degrees_in_radians = math.radians(degrees)
        cos = math.cos(degrees_in_radians)
        sin = math.sin(degrees_in_radians)
        x2 = round(self.x * cos - self.y * sin, 2)
        y2 = round(self.x * sin + self.y * cos, 2)
        return Vector(x2, y2)
