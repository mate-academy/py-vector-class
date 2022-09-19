import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other,
                          self.y * other)
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        vector_length = self.get_length()
        return Vector(self.x / vector_length,
                      self.y / vector_length)

    def angle_between(self, other):
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            length_self = self.get_length()
            length_other = other.get_length()
            cos_a = dot_product / (abs(length_self) * abs(length_other))
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        angle_y = math.atan2(self.x, self.y) * 180 / math.pi
        return round(abs(angle_y))

    def rotate(self, degrees: int):
        angle_in_radians = math.radians(degrees)
        new_x = round(self.x * math.cos(angle_in_radians) - self.y * math.sin(
            angle_in_radians), 2)
        new_y = round(self.x * math.sin(angle_in_radians) + self.y * math.cos(
            angle_in_radians), 2)
        return Vector(new_x, new_y)
