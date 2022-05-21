import math


class Vector:
    # write your code here
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other):
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, multiplier):
        if isinstance(multiplier, Vector):
            return (self.x * multiplier.x) + (self.y * multiplier.y)
        if isinstance(multiplier, int) or isinstance(multiplier, float):
            return Vector(
                round(self.x * multiplier, 2),
                round(self.y * multiplier, 2)
            )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        point_1 = end_point[0] - start_point[0]
        point_2 = end_point[1] - start_point[1]
        return Vector(
            round(point_1, 2),
            round(point_2, 2)
        )

    def get_length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self):
        the_length = self.get_length()
        return Vector(
            round(self.x / the_length, 2),
            round(self.y / the_length, 2)
        )

    def angle_between(self, other):
        vector_1_length = self.get_length()
        vector_2_length = other.get_length()
        dot_product = (self.x * other.x) + (self.y * other.y)
        cosinus = dot_product / (vector_1_length * vector_2_length)
        return round(math.degrees(math.acos(cosinus)))

    def get_angle(self):
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, angle):
        cosinus = math.cos(math.radians(angle))
        sinus = math.sin(math.radians(angle))
        x = self.x * cosinus - self.y * sinus
        y = self.x * sinus + self.y * cosinus
        return Vector(x, y)
