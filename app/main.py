from math import sqrt, acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(other * self.x, other * self.y)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def __get__(self):
        return self.get_length()

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return \
            cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(self.x / self.get_length(), (self.y / self.get_length()))

    def angle_between(self, other):
        if isinstance(other, Vector):
            product_of_length = self.get_length() * other.get_length()
            return round(degrees(acos(self * other / product_of_length)))

    def get_angle(self):
        return round(degrees(acos(self.y / self.get_length())))

    def rotate(self, degrees):
        x = self.x * cos(radians(degrees)) - self.y * sin(radians(degrees))
        y = self.x * sin(radians(degrees)) + self.y * cos(radians(degrees))
        return Vector(x, y)
