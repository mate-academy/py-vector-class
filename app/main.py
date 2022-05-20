import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other):
        self.x = round(self.x - (other.x), 2)
        self.y = round(self.y - (other.y), 2)
        return self

    def __mul__(self, other):
        if isinstance(other, Vector):
            product = self.x * other.x + (self.y * other.y)
            return product
        elif isinstance(other, (int, float)):
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
            return self

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x ** 2 + (self.y ** 2))

    def get_normalized(self):
        x = round(self.x / Vector.get_length(self), 2)
        y = round(self.y / Vector.get_length(self), 2)
        self.x = x
        self.y = y
        return self

    def angle_between(self, vector):
        length_self = Vector.get_length(self)
        length_vector = Vector.get_length(vector)
        product_length = length_self * length_vector
        cos_a = self.__mul__(vector) / product_length
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self):
        axis_y = Vector(0, abs(self.y))
        return self.angle_between(axis_y)

    def rotate(self, degrees: int):
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x = round(self.x * cos_a - self.y * sin_a, 2)
        y = round(self.x * sin_a + self.y * cos_a, 2)
        self.x = x
        self.y = y
        return self
