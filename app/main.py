import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other,
                      self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length,
                      self.y / length)

    def angle_between(self, other):
        cos_a = (self * other) / abs(self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        sine = math.sin(radians)
        cosine = math.cos(radians)
        return Vector(cosine * self.x - sine * self.y,
                      sine * self.x + cosine * self.y)
