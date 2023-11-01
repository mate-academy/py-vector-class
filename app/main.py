import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        return round(math.degrees(math.acos((self.x * other.x + self.y * other.y) / (self.get_length() * other.get_length()))))

    def get_angle(self):
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int):
        return Vector(math.cos(math.radians(degrees)) * self.x - math.sin(math.radians(degrees)) * self.y, math.sin(math.radians(degrees)) * self.x + math.cos(math.radians(degrees)) * self.y)
vector1 = Vector(33, 8)
vector2 = Vector(15, -76)
print(vector1.rotate(45).__dict__)
