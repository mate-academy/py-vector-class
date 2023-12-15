import math


class Vector:
    def __init__(self, x_coords, y_coords):
        self.x = round(x_coords, 2)
        self.y = round(y_coords, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_coords=self.x * other, y_coords=self.y * other)

    def __str__(self):
        return f"{self.x}, {self.y}"

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = round(end_point[0] - start_point[0], 2)
        y = round(end_point[1] - start_point[1], 2)
        return cls(x, y)

    def get_length(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 15)

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector):
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        cos_a = dot_product / (self.get_length() * other_vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return abs(round(angle_degrees))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
