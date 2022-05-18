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
        if isinstance(other, (float, int)):
            return Vector(
                self.x * other,
                self.y * other
            )
        else:
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        start_point = Vector(start_point[0], start_point[1])
        end_point = Vector(end_point[0], end_point[1])
        return end_point.__sub__(start_point)

    def get_length(self):
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self):
        length = self.get_length()
        x = round(self.x / length, 2)
        y = round(self.y / length, 2)
        return Vector(x, y)

    def angle_between(self, vector):
        dot_product = self.__mul__(vector)
        length_1 = self.get_length()
        length_2 = vector.get_length()
        cosine = dot_product / (length_1 * length_2)
        result = round(math.degrees(math.acos(cosine)))
        return result

    def get_angle(self):
        cosine = self.y / self.get_length()
        result = round(math.degrees(math.acos(cosine)))
        return result

    def rotate(self, degrees):
        degrees = math.radians(degrees)
        rotated_x = math.cos(degrees) * self.x - math.sin(degrees) * self.y
        rotated_y = math.sin(degrees) * self.x + math.cos(degrees) * self.y
        return Vector(rotated_x, rotated_y)
