import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: int | float) -> object:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float) -> object:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> object:
        if isinstance(other, (int, float)):
            return Vector(round((self.x * other), 2),
                          round((self.y * other), 2))
        if isinstance(other, Vector):
            new_vec = (self.x * other.x) + (self.y * other.y)
            return new_vec

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> object:
        return Vector((end_point[0] - start_point[0]),
                      (end_point[1] - start_point[1]))

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        result_1 = self * (1 / Vector.get_length(self))
        result_2 = self * (1 / Vector.get_length(self))
        return Vector(result_1.x, result_2.y)

    def angle_between(self, other: object) -> int:
        skolar = Vector.__mul__(self, other)
        modul_a = math.sqrt((self.x ** 2) + (self.y ** 2))
        modul_b = math.sqrt((other.x ** 2) + (other.y ** 2))
        cos_a = skolar / (modul_a * modul_b)
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> object:
        result = (self.x * 0) + (self.y * 1) / math.sqrt((self.x ** 2)
                                                         + (self.y ** 2)) * 1
        return math.floor(math.degrees(math.acos(result)))

    def rotate(self, degrees: int) -> object:
        rotated_x = (self.x * math.cos(math.radians(degrees))) - \
                    (self.y * math.sin(math.radians(degrees)))
        rotated_y = (self.x * math.sin(math.radians(degrees))) + \
                    (self.y * math.cos(math.radians(degrees)))
        return Vector(rotated_x, rotated_y)
