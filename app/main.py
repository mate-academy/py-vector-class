import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x,
                      self.y + other.y
                      )

    def __sub__(self, other):
        return Vector(self.x - other.x,
                      self.y - other.y
                      )

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(round(other * self.x, 2), round(other * self.y, 2))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, first, second):
        return cls(second[0] - first[0], second[1] - first[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        sec_len = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(self.__mul__(other) / sec_len)))

    def get_angle(self):
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees):
        cos_x = math.cos(math.radians(degrees)) * self.x
        cos_y = math.cos(math.radians(degrees)) * self.y
        sin_x = math.sin(math.radians(degrees)) * self.x
        sin_y = math.sin(math.radians(degrees)) * self.y
        return Vector(cos_x - sin_y, sin_x + cos_y)
