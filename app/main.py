import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=round((self.x - other.x), 2),
                      y=round((self.y - other.y), 2))

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(x=self.x * other,
                          y=self.y * other)
        else:
            Vector(x=self.x * other.x,
                   y=self.y * other.y)
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / Vector.get_length(self),
                      self.y / Vector.get_length(self))

    def angle_between(self, other):
        ab = self.x * other.x + self.y * other.y
        a = Vector.get_length(self)
        b = Vector.get_length(other)
        return round(math.degrees(math.acos(ab / (a * b))))

    def get_angle(self):
        other = Vector(0, 5)
        return Vector.angle_between(self, other)

    def rotate(self, degrees: int):
        x_cos = math.cos(math.radians(degrees))
        x_sin = math.sin(math.radians(degrees))
        return Vector(x=x_cos * self.x - x_sin * self.y,
                      y=x_sin * self.x + x_cos * self.y)
