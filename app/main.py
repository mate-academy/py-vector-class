import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x1, y1 = start_point
        x2, y2 = end_point
        return cls(x2 - x1, y2 - y1)

    def angle_between(self, other_vector):
        numerator = self * other_vector
        dominator = (self.get_length() * other_vector.get_length())
        return round(math.degrees(math.acos(numerator / dominator)))

    def get_angle(self):
        if self.y > 0:
            return self.angle_between(Vector(0, self.y))
        else:
            return self.angle_between(Vector(0, -self.y))

    def rotate(self, degrees):
        cos_x2 = math.cos(math.radians(degrees)) * self.x
        sin_x2 = math.sin(math.radians(degrees)) * self.y
        x2 = cos_x2 - sin_x2
        sin_y2 = math.sin(math.radians(degrees)) * self.x
        cos_y2 = math.cos(math.radians(degrees)) * self.y
        y2 = sin_y2 + cos_y2
        return Vector(x2, y2)
