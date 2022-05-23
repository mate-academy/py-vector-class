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
        if type(other) == int or type(other) == float:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector):
        cos_a = ((self.x * vector.x) + (self.y * vector.y)) / \
                (vector.get_length() * self.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = ((self.x * 0) + (self.y * 1)) / \
                (Vector(0, 1).get_length() * self.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle_x(self):
        cos_a = ((self.x * 1) + (self.y * 0)) / \
                (Vector(1, 0).get_length() * self.get_length())
        return math.degrees(math.acos(cos_a))

    def get_angle_y(self):
        cos_a = ((self.x * 0) + (self.y * 1)) / \
                (Vector(0, 1).get_length() * self.get_length())
        return math.degrees(math.acos(cos_a))

    def rotate(self, angle_rotate):
        if angle_rotate > 180:
            cos_a_b = math.cos(
                math.radians(angle_rotate) + math.radians(self.get_angle_y())
            )
            x2 = self.get_length() * cos_a_b
            sin_a_b = math.sin(
                math.radians(angle_rotate) + math.radians(self.get_angle_y())
            )
            y2 = self.get_length() * sin_a_b
            return Vector(-y2, x2)
        else:
            cos_a_b = math.cos(
                math.radians(angle_rotate) + math.radians(self.get_angle_x())
            )
            x2 = self.get_length() * cos_a_b
            sin_a_b = math.sin(
                math.radians(angle_rotate) + math.radians(self.get_angle_x())
            )
            y2 = self.get_length() * sin_a_b
            return Vector(x2, y2)
