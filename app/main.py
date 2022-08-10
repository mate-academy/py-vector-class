from math import sin, cos, acos, radians, degrees


class DicXY:
    def __init__(self, some_value):
        if isinstance(some_value, Vector):
            self.x = some_value.x
            self.y = some_value.y
        else:
            self.x = some_value
            self.y = some_value


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        uni_value = self.get_x_y(other)
        return Vector(self.x + uni_value.x, self.y + uni_value.y)

    def __sub__(self, other):
        uni_value = self.get_x_y(other)
        return Vector(self.x - uni_value.x, self.y - uni_value.y)

    def __mul__(self, other):
        uni_value = self.get_x_y(other)
        if not isinstance(other, Vector):
            return Vector(self.x * uni_value.x, self.y * uni_value.y)
        return self.x * uni_value.x + self.y * uni_value.y

    @staticmethod
    def get_x_y(some_value):
        return DicXY(some_value)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = (abs(self.x) ** 2 + abs(self.y) ** 2) ** 0.5
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector):
        mul = self * other_vector
        mul_vectors = self.get_length() * other_vector.get_length()
        return round(degrees(acos(mul / mul_vectors)))

    def get_angle(self):
        other_vector = Vector(0, abs(self.y))
        mul = self * other_vector
        mul_vectors = self.get_length() * other_vector.get_length()
        return round(degrees(acos(mul / mul_vectors)))

    def rotate(self, angle):
        angle = radians(angle)
        rotated_x = self.x * cos(angle) - self.y * sin(angle)
        rotated_y = self.x * sin(angle) + self.y * cos(angle)
        rot_vector = Vector(rotated_x, rotated_y)
        return rot_vector
