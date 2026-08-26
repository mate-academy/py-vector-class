import math


class Vector:
    def __init__(self, x_cord: (int, float), y_cord: (int, float)) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("You can only add vector objects")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("You can only sub vector objects")

    def __mul__(self, other: "Vector") -> ("Vector", int):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError("You can only multiply vector objects "
                        "or vector and int")

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def angle_between(self, other: "Vector") -> (int, float):

        cos_a = (((self.x * other.x) + (self.y * other.y))
                 / (math.sqrt(self.x ** 2 + self.y ** 2)
                     * math.sqrt(other.x ** 2 + other.y ** 2)))

        return round(math.degrees(math.acos(cos_a)))

    def get_length(self) -> (int, float):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def get_angle(self) -> (int, float):
        y_length = self.get_length()
        return self.angle_between(Vector(0, y_length))

    def rotate(self, degrees: (int, float)) -> object:

        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))

        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos

        return Vector(new_x, new_y)
