import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other):
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(other * self.x, 2), round(other * self.y, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other):
        return round(
            math.degrees(
                math.acos((self.x * other.x + self.y * other.y) / (
                    self.get_length() * math.sqrt(
                        other.x ** 2 + other.y ** 2)))), 0
        )

    def get_angle(self):
        angle = round(math.degrees(math.atan(abs(self.x) / abs(self.y))))
        print(angle, self.get_length(), self.x, self.y)
        if self.y < 0:
            return 180 - angle
        else:
            return angle

    def rotate(self, other):
        return Vector(
            round(self.x * math.cos(math.radians(other)) - self.y * math.sin(
                math.radians(other)), 2),
            round(self.y * math.cos(math.radians(other)) + self.x * math.sin(
                math.radians(other)), 2)
        )
