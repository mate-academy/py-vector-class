import math
import abc


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self):
        normal = 1 / self.get_length()
        return Vector(self.x * normal, self.y * normal)

    def angle_between(self, other):
        mul_len_vectors = self.get_length() * other.get_length()
        cos_between_vectors = (self * other) / mul_len_vectors
        return round(math.degrees(math.acos(cos_between_vectors)))

    def get_angle(self):
        cos = self.y / math.sqrt(self.x ** 2 + self.y ** 2)
        return round(math.degrees(math.acos(cos)))

    def rotate(self, other):
        angle = math.radians(other)
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.y * math.cos(angle) + self.x * math.sin(angle)
        return Vector(x, y)
