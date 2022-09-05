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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_between(self, other):
        cos = (self.x * other.x + self.y * other.y) / \
              (Vector.get_length(self) * Vector.get_length(other))
        return round(math.degrees(math.acos(cos)))

    def get_angle(self):
        cos_a = (self.x * 0 + self.y * 1) / \
                (Vector.get_length(self) * ((0 ** 2 + 1 ** 2) ** 0.5))
        return round(math.degrees(math.acos(cos_a)))

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def rotate(self, degrees):
        sin = (math.sin(math.radians(degrees)))
        cos = (math.cos(math.radians(degrees)))
        return Vector(self.x * cos - self.y * sin,
                      self.y * cos + self.x * sin)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])
