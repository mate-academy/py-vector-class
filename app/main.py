import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vec_2):
        return Vector(self.x + vec_2.x, self.y + vec_2.y)

    def __sub__(self, vec_2):
        return Vector(self.x - vec_2.x, self.y - vec_2.y)

    def __mul__(self, vec_2):
        if isinstance(vec_2, (int, float)):
            return Vector(self.x * vec_2, self.y * vec_2)
        if isinstance(vec_2, Vector):
            return self.x * vec_2.x + self.y * vec_2.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple):
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vec_2):
        angl = self.__mul__(vec_2) / (self.get_length() * vec_2.get_length())
        angl = round(math.degrees(math.acos(angl)))
        return angl

    def get_angle(self):
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, deg):
        x = math.cos(math.radians(deg)) * self.x - math.sin(math.radians(deg)) * self.y
        y = math.sin(math.radians(deg)) * self.x + math.cos(math.radians(deg)) * self.y
        return Vector(x, y)
