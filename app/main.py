import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        a = end_point[0] - start_point[0]
        b = end_point[1] - start_point[1]
        return cls(a, b)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        inv_length = 1 / round(Vector.get_length(self), 2)
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other):
        mult_len = Vector.get_length(self) * Vector.get_length(other)
        cos = Vector.__mul__(self, other) / mult_len
        return round(math.degrees(math.acos(cos)))

    def get_angle(self):
        y_axis = Vector(0, abs(self.y))
        mult_len = Vector.get_length(self) * Vector.get_length(y_axis)
        cos = Vector.__mul__(self, y_axis) / mult_len
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degree):
        cos_rotate = math.cos(math.radians(degree))
        sin_rotate = math.sin(math.radians(degree))
        new_x = cos_rotate * self.x - sin_rotate * self.y
        new_y = sin_rotate * self.x + cos_rotate * self.y
        return Vector(round(new_x, 2), round(new_y, 2))
