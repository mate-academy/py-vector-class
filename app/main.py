import math


class Vector:
    def create_vector_by_two_points(start_point, end_point):
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return NotImplemented

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            raise ValueError("Неможливо обчислити")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError(" ")
        dot_prod = self * other
        cos_angle = dot_prod / (len_self * len_other)
        cos_angle = max(min(cos_angle, 1), -1)
        return math.degrees(math.acos(cos_angle))

    def get_angle(self):
        length = self.get_length()
        angle = math.acos = self.y / length()
        angle_degrees = math.degrees(angle)
        return angle_degrees

    def rotate(self, angle):
        a_cos = math.cos(angle)
        b_sin = math.sin(angle)
        x_x = a_cos * self.x - self.y * b_sin
        y_y = b_sin * self.x + self.y * a_cos
        x_x_degrees = math.degrees(x_x)
        y_y_degrees = math.degrees(y_y)
        vector = x_x_degrees, y_y_degrees
        return vector
