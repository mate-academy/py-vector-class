import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=self.x + other.x, y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x, y=self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(x=self.x * other, y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(x=end_point[0] - start_point[0],
                      y=end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length())

    def angle_between(self, other):
        mult_length = self.get_length() * other.get_length()
        cos_a = Vector.__mul__(self, other) / mult_length
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)), 0)

    def rotate(self, degrees):
        a_rad = math.radians(degrees)
        return Vector(x=math.cos(a_rad) * self.x - math.sin(a_rad) * self.y,
                      y=math.sin(a_rad) * self.x + math.cos(a_rad) * self.y)
