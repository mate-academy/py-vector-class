import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        l = self.get_length()
        return Vector(self.x / l, self.y / l)

    def angle_between(self, other):
        cos_a = (self.x * other.x + self.y * other.y) / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(cos_a))))

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return int(round(math.degrees(math.acos(cos_a))))

    def rotate(self, degrees):
        r = math.radians(degrees)
        x = self.x * math.cos(r) - self.y * math.sin(r)
        y = self.x * math.sin(r) + self.y * math.cos(r)
        return Vector(x, y)
