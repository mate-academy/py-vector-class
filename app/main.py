import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector):
        if isinstance(vector, Vector):
            vector.x = self.x + vector.x
            vector.y = self.y + vector.y
            return Vector(vector.x, vector.y)

    def __sub__(self, vector):
        if isinstance(vector, Vector):
            vector.x = self.x - vector.x
            vector.y = self.y - vector.y
            return Vector(vector.x, vector.y)

    def __mul__(self, vector):
        if vector == 0:
            return Vector(0, 0)
        if isinstance(vector, float):
            self.x = self.x * vector
            self.y = self.y * vector
            return Vector(self.x, self.y)

        if isinstance(vector, Vector):
            vector.x = self.x * vector.x
            self.y = self.y * vector.y
            return vector.x + self.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x=x, y=y)

    def get_length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector):
        mul_of_vectors = (self.x * vector.x + self.y * vector.y)
        len_x = math.sqrt(self.x**2 + self.y**2)
        len_y = math.sqrt(vector.x**2 + vector.y**2)
        cos = mul_of_vectors / (len_x * len_y)
        return round(math.degrees(math.acos(cos)))

    def get_angle(self):
        y_axis = (0, 1)
        mul_of_vectors = (self.x * y_axis[0] + self.y * y_axis[1])
        len_x = math.sqrt(self.x ** 2 + self.y ** 2)
        len_y = math.sqrt(y_axis[0] ** 2 + y_axis[1] ** 2)
        cos = mul_of_vectors / (len_x * len_y)
        return round(math.degrees(math.acos(cos)))

    def rotate(self, degrees):
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        rotated_x = self.x * cos - self.y * sin
        rotated_y = self.x * sin + self.y * cos
        return Vector(rotated_x, rotated_y)
