from math import cos, sin, radians, degrees, acos, atan2


class Vector:
    def __init__(self, x=0.0, y=0.0):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(round((self.x + other.x), 2),
                      round((self.y + other.y), 2))

    def __sub__(self, other):
        return Vector(round((self.x - other.x), 2),
                      round((self.y - other.y), 2))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        if isinstance(other, (int, float)):
            return Vector(round((self.x * other), 2),
                          round((self.y * other), 2))

    @staticmethod
    def create_vector_by_two_points(start_point: tuple, end_point: tuple):
        return Vector(round((start_point[0] - end_point[0]) * -1, 2),
                      round((start_point[1] - end_point[1]) * -1, 2))

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(round((self.x / Vector.get_length(self)), 2),
                      round((self.y / Vector.get_length(self)), 2))

    def angle_between(self, vector):
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self):
        return abs(round(degrees(atan2(self.x, self.y))))

    def rotate(self, degrees):
        cosine = cos(radians(degrees))
        sine = sin(radians(degrees))
        return Vector(cosine * self.x - sine * self.y,
                      sine * self.x + cosine * self.y)
