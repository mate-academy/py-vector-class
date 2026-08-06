import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        print(self.get_length())
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return Vector(x, y)

    def angle_between(self, other_vector):
        dot_vectors = self.x * other_vector.x + self.y * other_vector.y
        abs_a = math.sqrt(self.x ** 2 + self.y ** 2)
        abs_b = math.sqrt(other_vector.x ** 2 + other_vector.y ** 2)
        cos_a = round(math.degrees(math.acos(dot_vectors / (abs_a * abs_b))))
        return cos_a

    def get_angle(self):
        cos_a = self.y / math.sqrt(self.x ** 2 + self.y ** 2)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        degrees_to_radian = math.radians(degrees)
        cos_degrees = math.cos(degrees_to_radian)
        sin_degrees = math.sin(degrees_to_radian)
        rotated_x = self.x * cos_degrees - self.y * sin_degrees
        rotated_y = self.y * cos_degrees + self.x * sin_degrees
        return Vector(rotated_x, rotated_y)
