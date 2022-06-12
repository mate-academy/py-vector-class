import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other):
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        vector_start = cls(start_point[0], start_point[1])
        vector_end = cls(end_point[0], end_point[1])
        return cls.__sub__(vector_end, vector_start)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            (self.x / Vector.get_length(self)),
            (self.y / Vector.get_length(self))
        )

    def angle_between(self, other):
        a = Vector.__mul__(self, other)
        b = Vector.get_length(self) * Vector.get_length(other)
        cos_a = a / b
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        axis_y = Vector(0, 1)
        a = Vector.__mul__(self, axis_y)
        b = Vector.get_length(self) * Vector.get_length(axis_y)
        cos_a = a / b
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degree):
        angle = math.radians(degree)
        x = self.x * math.cos(angle) - self.y * math.sin(angle)
        y = self.y * math.cos(angle) + self.x * math.sin(angle)
        return Vector(x, y)
