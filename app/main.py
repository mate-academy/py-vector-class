import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x * self.x + self.y * self.y) ** 0.5

    def get_normalized(self):
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other):
        dot_product = self * other
        mult_lengths = self.get_length() * other.get_length()
        cos_a = dot_product / mult_lengths
        return round((math.degrees((math.acos(cos_a)))))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        new_y = math.sin(radians) * self.x + math.cos(radians) * self.y

        return Vector(new_x, new_y)
