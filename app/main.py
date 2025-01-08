from math import acos, degrees, radians, cos, sin, sqrt


class Vector:
    def __init__(self, coord_x, coord_y):
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __add__(self, other):
        return Vector(self.coord_x + other.coord_x, self.coord_y + other.coord_y)

    def __sub__(self, other):
        return Vector(self.coord_x - other.coord_x, self.coord_y - other.coord_y)

    def __mul__(self, value):
        if isinstance(value, (int, float)):
            return Vector(self.coord_x * value, self.coord_y * value)
        if isinstance(value, Vector):
            return round(self.coord_x * value.coord_x + self.coord_y * value.coord_y, 4)
        raise ValueError("Multiplication with type not supported")

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return sqrt(self.coord_x ** 2 + self.coord_y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.coord_x / length, self.coord_y / length)

    def angle_between(self, other):
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = max(-1, min(1, dot_product / lengths_product))
        return round(degrees(acos(cos_angle)))

    def get_angle(self):
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees_to_rotate):
        angle_radians = radians(degrees_to_rotate)
        rotated_x = (self.coord_x * cos(angle_radians) -
                     self.coord_y * sin(angle_radians))
        rotated_y = (self.coord_x * sin(angle_radians) +
                     self.coord_y * cos(angle_radians))
        return Vector(rotated_x, rotated_y)


