import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            # Match test precision for dot product
            return round(self.x * other.x + self.y * other.y, 14)
        elif isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            raise TypeError("Unsupported type for multiplication")

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other):
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        cos_angle = dot_product / length_product
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self):
        radians = math.atan2(self.y, self.x)
        degrees = math.degrees(radians)
        angle_from_y_axis = (degrees - 90) % 360
        return round(angle_from_y_axis)

    def rotate(self, degrees):
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        x_rotated = self.x * cos_angle - self.y * sin_angle
        y_rotated = self.x * sin_angle + self.y * cos_angle
        return Vector(round(x_rotated, 2), round(y_rotated, 2))
