import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        self.x = round((self.x + other.x), 2)
        self.y = round((self.y + other.y), 2)
        return self

    def __sub__(self, other):
        self.x = round((self.x - other.x), 2)
        self.y = round((self.y - other.y), 2)
        return self

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.x = round((self.x * other.real), 2)
            self.y = round((self.y * other.real), 2)
            return self
        self.x = self.x * other.x
        self.y = self.y * other.y
        dot_product = self.x + self.y
        return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return cls(point_x, point_y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        self.x = round((self.x / length), 2)
        self.y = round((self.y / length), 2)
        return self

    def angle_between(self, other):
        first = (self.x * other.x) + (self.y * other.y)
        length_mult = self.get_length() * other.get_length()
        cos_a = first / length_mult
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self):
        positive_y = Vector(0, 5)
        first = (self.x * positive_y.x) + (self.y * positive_y.y)
        length_mult = self.get_length() * positive_y.get_length()
        cos_a = first / length_mult
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, angle: int):
        converted = math.radians(angle)
        new_x = math.cos(converted) * self.x - math.sin(converted) * self.y
        new_y = math.sin(converted) * self.x + math.cos(converted) * self.y
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)
        return self
