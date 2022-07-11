import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple, end_point: tuple):
        return Vector(x=end_point[0] - start_point[0],
                      y=end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector):
        if isinstance(other_vector, Vector):
            scalar = self * other_vector
            mult_len = self.get_length() * other_vector.get_length()
            cos_a = scalar / mult_len
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, angle):
        rad_angle = math.radians(angle)
        x2 = self.x * math.cos(rad_angle) - self.y * math.sin(rad_angle)
        y2 = self.x * math.sin(rad_angle) + self.y * math.cos(rad_angle)
        return Vector(x2, y2)
