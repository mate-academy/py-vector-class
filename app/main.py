import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, v2):
        return Vector(self.x + v2.x, self.y + v2.y)

    def __sub__(self, v2):
        return Vector(self.x - v2.x, self.y - v2.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        other_len = math.sqrt(other.x ** 2 + other.y ** 2)
        return round(
            math.degrees(math.acos(self.__mul__(other) / (
                self.get_length() * other_len))))

    def get_angle(self):
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degree):
        radian = math.radians(degree)
        return Vector(x=math.cos(radian) * self.x - math.sin(radian) * self.y,
                      y=math.sin(radian) * self.x + math.cos(radian) * self.y)
