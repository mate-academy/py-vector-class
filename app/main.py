import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + other.y * self.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, vector2):
        cos_a = (self * vector2) / (self.get_length() * vector2.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int):
        rad = math.radians(degrees)
        return Vector(self.x * math.cos(rad) - self.y * math.sin(rad),
                      self.x * math.sin(rad) + self.y * math.cos(rad))
