import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if not isinstance(other, Vector):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        multiply = self.x * other.x + self.y * other.y
        return multiply

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        unit_vector = self.get_length()
        self.x /= unit_vector
        self.y /= unit_vector
        return Vector(self.x, self.y)

    def angle_between(self, vector):
        cos_a = self.__mul__(vector) / (self.get_length() * vector.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self):
        vector = Vector(0, abs(self.y))
        return self.angle_between(vector)

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = round(math.cos(radians) * self.x - math.sin(radians) * self.y, 2)
        new_y = round(math.sin(radians) * self.x + math.cos(radians) * self.y, 2)
        return Vector(new_x, new_y)
