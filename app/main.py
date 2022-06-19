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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / Vector.get_length(self),
                      self.y / Vector.get_length(self))

    def angle_between(self, other):
        vector_mul = Vector.__mul__(self, other)
        length_mul = Vector.get_length(self) * Vector.get_length(other)
        cos_a = vector_mul / length_mul
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        other = Vector(0, 1)
        return Vector.angle_between(self, other)

    def rotate(self, degrees):
        rad = math.radians(degrees)
        x = self.x * math.cos(rad) - self.y * math.sin(rad)
        y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(x, y)

    pass
