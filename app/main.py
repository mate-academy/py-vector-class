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
        if isinstance(other, Vector):
            product_x = self.x * other.x
            product_y = self.y * other.y
            return product_x + product_y

        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start, end):
        return cls(
            end[0] - start[0],
            end[1] - start[1]
        )

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector_2):
        dot_product = self.__mul__(vector_2)
        len_product = abs(self.get_length()) * abs(vector_2.get_length())
        angle = dot_product / len_product
        return round(math.degrees(math.acos(angle)))

    def get_angle(self):
        # y_axis = (0, 1)
        return self.angle_between(Vector(0, 1))

    def rotate(self, spin):
        new_x = math.cos(math.radians(spin)) * self.x - \
            math.sin(math.radians(spin)) * self.y
        new_y = math.sin(math.radians(spin)) * self.x + \
            math.cos(math.radians(spin)) * self.y
        return Vector(new_x, new_y)
