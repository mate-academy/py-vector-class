import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, other):
        vec1_mul_vec2 = self * other
        len_vec1_mul_len_vec2 = self.get_length() * other.get_length()
        cos_of_angle = vec1_mul_vec2 / len_vec1_mul_len_vec2
        return round(math.degrees(math.acos(cos_of_angle)))

    def get_angle(self):
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int):
        angle = math.radians(degrees)
        return Vector(
            x=math.cos(angle) * self.x - math.sin(angle) * self.y,
            y=math.sin(angle) * self.x + math.cos(angle) * self.y
        )
