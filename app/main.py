import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, multipler):
        if isinstance(multipler, Vector):
            return self.x * multipler.x + self.y * multipler.y
        return Vector(x=self.x * multipler, y=self.y * multipler)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return Vector(x, y)

    def get_angle(self):
        cos_a = self.y / (self.x ** 2 + self.y ** 2) ** 0.5
        return round(math.degrees(math.acos(cos_a)))

    def angle_between(self, vector):
        ax = self.x
        ay = self.y
        bx = vector.x
        by = vector.y
        cos_a = (ax * bx + ay * by) / \
                ((ax ** 2 + ay ** 2) ** 0.5 * (bx ** 2 + by ** 2) ** 0.5)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle):
        x = math.cos(math.radians(angle)) * \
            self.x - math.sin(math.radians(angle)) * self.y
        y = math.sin(math.radians(angle)) * \
            self.x + math.cos(math.radians(angle)) * self.y
        return Vector(x, y)
