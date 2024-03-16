import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: object) -> object:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: object) -> object:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: float | object) -> object | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start_poit: tuple,
                                    end_point: tuple) -> object:
        return Vector((end_point[0] - start_poit[0]),
                      (end_point[1] - start_poit[1]))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: object) -> float:
        dot_product = self.__mul__(other)
        length_product = self.get_length() * other.get_length()
        cos_a = dot_product / length_product
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> object:
        dot_product = self.__mul__(Vector(0, 1))
        length_product = self.get_length() * Vector(0, 1).get_length()
        cos_a = dot_product / length_product
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> object:
        radians = math.radians(degrees)
        x_coord = (self.x * math.cos(radians)
                   - self.y * math.sin(radians))
        y_coord = (self.x * math.sin(radians)
                   + self.y * math.cos(radians))
        return Vector(x_coord, y_coord)
