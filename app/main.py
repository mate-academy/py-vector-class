import math


class Vector:

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            vect_dot = self.x * other.x + self.y * other.y
            return vect_dot

        self.x = round(self.x * other, 2)
        self.y = round(self.y * other, 2)
        return self

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()

        return Vector(x, y)

    def angle_between(self, other):
        angle_cos = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self):
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, degree):
        angle_rad = math.radians(degree)
        x_2 = math.cos(angle_rad) * self.x - math.sin(angle_rad) * self.y
        y_2 = math.sin(angle_rad) * self.x + math.cos(angle_rad) * self.y

        return Vector(x_2, y_2)
