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
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (float, int)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        x = self.x / self.get_length()
        y = self.y / self.get_length()

        return Vector(x, y)

    def angle_between(self, other):
        angle_cos = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotation_degree):
        radius = math.radians(rotation_degree)

        return Vector(
            x=self.x * math.cos(radius) - self.y * math.sin(radius),
            y=self.x * math.sin(radius) + self.y * math.cos(radius),
        )
