import math


class Vector:
    def __init__(self, x_val: float, y_val: float) -> None:
        self.x = round(x_val, 2)
        self.y = round(y_val, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector | float | int")\
            -> "Vector | float | int":
        if isinstance(other, float | int):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point : tuple,
                                    end_point : tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: "Vector") -> int:
        angle = self.__mul__(other) / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(angle)), 0))

    def get_angle(self) -> int:
        positive_y_vector = Vector(0, 1)
        return self.angle_between(positive_y_vector)

    def rotate(self, degrees : int) -> "Vector":
        degrees = math.radians(degrees)
        x_cord = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        y_cord = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(round(x_cord, 2), round(y_cord, 2))
