import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return Vector(x, y)

    def angle_between(self, vector):
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_b = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_b)))

    def rotate(self, degrees):
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        x_2 = cos * self.x - sin * self.y
        y_2 = cos * self.y + sin * self.x
        return Vector(x_2, y_2)
