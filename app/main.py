from math import degrees, acos, sqrt, radians, cos, sin


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if type(other) in (int, float):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(x=self.x / self.get_length(),
                      y=self.y / self.get_length())

    def angle_between(self, other):
        return round(degrees(acos(
            ((self * other) / (sqrt(self.get_length() ** 2
                                    ) * sqrt(other.get_length() ** 2))))))

    def get_angle(self):
        return round(degrees(acos(((self.y) / (self.get_length())))))

    def rotate(self, angle):
        x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        y = self.x * sin(radians(angle)) + self.y * cos(radians((angle)))
        return Vector(x, y)
