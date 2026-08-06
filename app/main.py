import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        if isinstance(other, Vector):
            product = self * other
            cosine = product / (self.get_length() * other.get_length())
            return round(math.degrees(math.acos(cosine)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree):
        radians = math.radians(degree)
        x = math.cos(radians) * self.x - math.sin(radians) * self.y
        y = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(x, y)
