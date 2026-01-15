import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other):
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(x=self.x * other, y=self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple):
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self):
        return abs((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self):
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length())

    def angle_between(self, vector):
        return round(math.degrees(math.acos(
            self.__mul__(vector) / (self.get_length() * vector.get_length()))))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int):
        return Vector(math.cos(math.radians(degrees)) * self.x - math.sin(
                      math.radians(degrees)) * self.y,
                      math.sin(math.radians(degrees)) * self.x + math.cos(
                      math.radians(degrees)) * self.y)
