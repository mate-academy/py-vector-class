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
            return self.x * other.x + self.y * other.y
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start, end):
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        length = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(self * other / length)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, grad):
        rad = math.radians(grad)
        return Vector(
            math.cos(rad) * self.x - math.sin(rad) * self.y,
            math.sin(rad) * self.x + math.cos(rad) * self.y
        )
