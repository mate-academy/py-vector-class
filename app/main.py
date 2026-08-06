import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other,
                          self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple):
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self):
        vector_length = self.get_length()
        new_x = self.x / vector_length
        new_y = self.y / vector_length
        return Vector(new_x, new_y)

    def angle_between(self, other):
        mul_of_lengths = self.get_length() * other.get_length()
        cos_a = self * other / mul_of_lengths
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        cos_a = math.cos(math.radians(degrees))
        sin_a = math.sin(math.radians(degrees))
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
