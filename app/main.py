import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            x=(start_point[0] - end_point[0]) * -1,
            y=(start_point[1] - end_point[1]) * -1
        )

    def get_length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self):
        return Vector(
            x=self.x / Vector.get_length(self),
            y=self.y / Vector.get_length(self)
        )

    def angle_between(self, vector):
        dot_product = self * vector
        cos_a = dot_product / \
            (Vector.get_length(self) * Vector.get_length(vector))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        return Vector(
            x=self.x * math.cos(radians) - self.y * math.sin(radians),
            y=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
