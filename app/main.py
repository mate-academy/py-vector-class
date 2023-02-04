from math import sqrt, acos, degrees, fabs, sin, cos, radians


class Vector:
    def __init__(self, x: (int, float), y: (int, float)):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other):
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, *args):
        other = args[0]
        if isinstance(other, Vector):
            return other.x * self.x + other.y * self.y
        if isinstance(other, (float, int)):
            return Vector(other * self.x, other * self.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector((end_point[0] - start_point[0]), (end_point[1] - start_point[1]))

    def get_length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other_vector):
        mod_of_vector = sqrt(self.x ** 2 + self.y ** 2) * sqrt(other_vector.x ** 2 + other_vector.y ** 2)
        dotproduct = self.x * other_vector.x + self.y * other_vector.y
        return round(degrees(acos(dotproduct / mod_of_vector)))

    def get_angle(self):
        other_vector = Vector(0, fabs(self.y))
        return self.angle_between(other_vector)

    def rotate(self, degrees):
        angle = radians(degrees)
        x2 = cos(angle) * self.x - sin(angle) * self.y
        y2 = sin(angle) * self.x + cos(angle) * self.y
        return Vector(x2, y2)
