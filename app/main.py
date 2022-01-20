import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            self.x = self.x + other.x
            self.y = self.y + other.y
            return Vector(self.x, self.y)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.x = self.x - other.x
            self.y = self.y - other.y
            return Vector(self.x, self.y)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            self.x = self.x * other
            self.y = self.y * other
            return Vector(self.x, self.y)
        else:
            raise TypeError

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0], end_point[1]).__sub__(cls(start_point[0], start_point[1]))

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other):
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        point_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        point_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(point_x, point_y)
