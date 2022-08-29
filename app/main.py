import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(x=end_point[0] - start_point[0],
                   y=end_point[1] - start_point[1])

    def get_length(self):
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self):
        loc_length = 1 / self.get_length()
        self.x = self.x * loc_length
        self.y = self.y * loc_length
        return Vector(self.x, self.y)

    def angle_between(self, other):
        scal_prod = (self.x * other.x) + (self.y * other.y)
        cos_a = scal_prod / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        scal_prod = (self.y * self.y)
        cos_a = scal_prod / ((self.x**2 + self.y**2)**0.5 * self.y)
        return int(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        return Vector(x=self.x * cos_a - self.y * sin_a,
                      y=self.x * sin_a + self.y * cos_a)
