from math import sqrt, pow, degrees, acos, sin, cos, radians


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
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self):
        length_ = self.get_length()
        self.x = round(self.x / length_, 2)
        self.y = round(self.y / length_, 2)
        return self

    def angle_between(self, vector):
        cos_ = self * vector / (self.get_length() * vector.get_length())
        return round(degrees(acos(cos_)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, agree):
        x = cos(radians(agree)) * self.x - sin(radians(agree)) * self.y
        y = sin(radians(agree)) * self.x + cos(radians(agree)) * self.y
        return Vector(x, y)
