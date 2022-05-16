import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(round(x, 2), round(y, 2))

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x = self.x * other
            y = self.y * other
            return Vector(round(x, 2), round(y, 2))
        dot_product = self.x * other.x + self.y * other.y
        return dot_product

    def get_length(self):
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return Vector(x, y)

    def angle_between(self, vector):
        length = self.get_length() * vector.get_length()
        cos_a = self * vector / length
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        angle = self.angle_between(Vector(0, abs(self.y)))
        return angle

    def rotate(self, degrees):
        radians = math.radians(degrees)
        x = math.cos(radians) * self.x - math.sin(radians) * self.y
        y = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(x, y)
