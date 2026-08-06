import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            x=round(self.x * other, 2),
            y=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self):
        vector_length = Vector.get_length(self)
        return Vector(
            x=round(self.x / vector_length, 2),
            y=round(self.y / vector_length, 2)
        )

    def angle_between(self, other):
        vector_for_product = Vector.__mul__(self, other)
        if isinstance(vector_for_product, Vector):
            product_of_vectors = vector_for_product.x + vector_for_product.y
        else:
            product_of_vectors = vector_for_product
        product_of_lengths = Vector.get_length(self) * Vector.get_length(other)
        cos = product_of_vectors / product_of_lengths
        return round(math.degrees(math.acos(cos)))

    def get_angle(self):
        positive_y_axis_vector = Vector(0, 1)
        return Vector.angle_between(self, positive_y_axis_vector)

    def rotate(self, degree):
        radians = math.radians(degree)
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            x=round((cos * self.x - sin * self.y), 2),
            y=round((sin * self.x + cos * self.y), 2)
        )
