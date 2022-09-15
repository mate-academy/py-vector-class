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
            new_x = self.x * other.x
            new_y = self.y * other.y
            return new_x + new_y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other):
        #           a * b
        # arccos (------------)
        #          |a| * |b|
        numeral = self.__mul__(other)
        banner = abs(self.get_length()) * abs(other.get_length())
        angle = numeral / banner
        return round(math.degrees(math.acos(angle)))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees):
        sin = math.sin(math.radians(degrees))
        cos = math.cos(math.radians(degrees))
        new_x = cos * self.x - sin * self.y
        new_y = sin * self.x + cos * self.y
        return Vector(new_x, new_y)
