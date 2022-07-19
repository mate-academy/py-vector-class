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
        return (self.x * other.x + self.y * other.y
                if isinstance(other, Vector)
                else Vector(self.x * other, self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        x = self.x / math.sqrt(self.x ** 2 + self.y ** 2)
        y = self.y / math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(x, y)

    def angle_between(self, other):
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        cos_a = dot_product / (length_self * length_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        cs = math.cos(math.radians(degrees))
        sn = math.sin(math.radians(degrees))
        x = self.x * cs - self.y * sn
        y = self.x * sn + self.y * cs
        return Vector(x, y)
