from math import sqrt, degrees, acos, cos, sin, radians


# update progress
class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) is Vector:
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other):
        if isinstance(other, Vector):
            other_vector_mod = sqrt((other.x ** 2) + (other.y ** 2))
            cos_a = self * other / (self.get_length() * other_vector_mod)
            return round(degrees(acos(cos_a)))
        raise TypeError(f"Uncorrected type {other} : {type(other)}."
                        f"Must be {Vector}")

    def get_angle(self):
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, angle):
        x2 = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        y2 = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
        return Vector(x2, y2)
