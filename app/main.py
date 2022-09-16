import math


class Vector:
    def __init__(self, x, y) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, new_vector):
        return Vector(self.x + new_vector.x, self.y + new_vector.y)

    def __sub__(self, new_vector):
        return Vector(self.x - new_vector.x, self.y - new_vector.y)

    def __mul__(self, new_vector):
        if isinstance(new_vector, Vector):
            result = self.x * new_vector.x, self.y * new_vector.y
            return sum(result)
        if isinstance(new_vector, (int, float)):
            return Vector(self.x * new_vector, self.y * new_vector)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self):
        locLength = self.get_length()
        inv_length = 1 / locLength
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, new):
        res = (self.x * new.x + self.y * new.y) / (
            abs(self.get_length()) * abs(Vector.get_length(new))
        )
        return math.ceil(math.degrees(math.acos(res)))

    def get_angle(self):
        new = Vector(0, 1)
        res = (self.x * new.x + self.y * new.y) / (
            abs(self.get_length()) * abs(Vector.get_length(new))
        )
        return math.floor(math.degrees(math.acos(res)))

    def rotate(self, angle):
        angle_radian = math.radians(angle)
        angle_cos = math.cos(angle_radian)
        angle_sin = math.sin(angle_radian)
        res_x = self.x * angle_cos - self.y * angle_sin
        res_y = self.x * angle_sin + self.y * angle_cos
        return Vector(round(res_x, 2), round(res_y, 2))
