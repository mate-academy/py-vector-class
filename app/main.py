import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        new_vector = Vector(new_x, new_y)
        return new_vector

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        new_x = self.x / self.get_length()
        new_y = self.y / self.get_length()
        return Vector(new_x, new_y)

    def angle_between(self, other):
        a = self * other
        b = self.get_length() * other.get_length()
        c = a / b
        return round(math.degrees(math.acos(c)))

    def get_angle(self):
        other = Vector(x=0, y=1)
        return round(self.angle_between(other))

    def rotate(self, degrees):
        a = self.x * math.cos(math.radians(degrees))
        b = self.y * math.sin(math.radians(degrees))
        new_x = a - b
        c = self.x * math.sin(math.radians(degrees))
        d = self.y * math.cos(math.radians(degrees))
        new_y = c + d
        return Vector(new_x, new_y)
