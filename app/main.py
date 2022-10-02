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
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other):
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length())
        )))

    def get_angle(self):
        return round(math.degrees(math.acos(
            (self * Vector(0, 1)) / self.get_length()
        )))

    def rotate(self, angle):
        ange_rad = angle * math.pi / 180
        return Vector(
            round(
                self.x * math.cos(ange_rad) - self.y * math.sin(ange_rad), 2
            ),
            round(
                self.x * math.sin(ange_rad) + self.y * math.cos(ange_rad), 2
            )
        )
