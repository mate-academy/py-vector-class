import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=self.x * other,
            y=self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x1 = end_point[0]
        x2 = start_point[0]
        y1 = end_point[1]
        y2 = start_point[1]
        return cls.__sub__(cls(x1, y1), cls(x2, y2))

    def get_length(self):
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self):
        normalize = 1 / self.get_length()
        return Vector(
            x=self.x * normalize,
            y=self.y * normalize,
        )

    def angle_between(self, vector):
        mul_mod_vectors = self.get_length() * vector.get_length()
        cos_between_vectors = (self * vector) / mul_mod_vectors
        angle = round(math.degrees(math.acos(cos_between_vectors)))
        return angle

    def get_angle(self):
        pos_y = Vector(0, 1)
        return self.angle_between(pos_y)

    def rotate(self, degrees):
        rad = math.radians(degrees)
        rotated_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        rotated_y = self.y * math.cos(rad) + self.x * math.sin(rad)
        return Vector(
            x=rotated_x,
            y=rotated_y,
        )
