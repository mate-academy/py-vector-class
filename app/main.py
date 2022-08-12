import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def create_vector_by_two_points(self, other):
        self = list(self)
        other = list(other)
        return Vector(other[0] - self[0], other[1] - self[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other):
        length_self = (self.x ** 2 + self.y ** 2) ** 0.5
        length_other = (other.x ** 2 + other.y ** 2) ** 0.5
        multiplication = self.x * other.x + self.y * other.y
        cos_a = multiplication / (length_self * length_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / ((self.x ** 2 + self.y ** 2) ** 0.5)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle):
        x_coordinate_first_part = math.cos(math.radians(angle)) * self.x
        x_coordinate_second_part = math.sin(math.radians(angle)) * self.y
        y_coordinate_first_part = math.sin(math.radians(angle)) * self.x
        y_coordinate_second_part = math.cos(math.radians(angle)) * self.y
        x_coordinate = x_coordinate_first_part - x_coordinate_second_part
        y_coordinate = y_coordinate_first_part + y_coordinate_second_part
        return Vector(x_coordinate, y_coordinate)
