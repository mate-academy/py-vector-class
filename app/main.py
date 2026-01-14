import math


class Vector:

    def __init__(self, x: int, y: int):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, point):
        return Vector(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Vector(self.x - point.x, self.y - point.y)

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: set,
                                    end_point: set):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self):
        return Vector(self.x * 1 / self.get_length(),
                      self.y * 1 / self.get_length())

    def angle_between(self, point):
        len_self = ((self.x ** 2) + (self.y ** 2)) ** 0.5
        len_point = ((point.x ** 2) + (point.y ** 2)) ** 0.5
        cos_a = self.__mul__(point) / (len_self * len_point)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = (self.x * 0 + self.y * 1) / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        cos_f = math.cos(math.radians(degrees))
        sin_f = math.sin(math.radians(degrees))
        x = round((self.x * cos_f) - (self.y * sin_f), 2)
        y = round((self.x * sin_f) + (self.y * cos_f), 2)
        return Vector(x, y)
