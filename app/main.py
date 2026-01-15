import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vector' or float) -> 'Vector' or float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 4)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> 'Vector':
        x_delta = end_point[0] - start_point[0]
        y_delta = end_point[1] - start_point[1]
        return cls(x_delta, y_delta)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> 'Vector':
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: 'Vector') -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0

        cos_a = dot_product / length_product
        cos_a = max(-1.0, min(1.0, cos_a))

        return int(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_axis_vector = Vector(0, 1)
        dot_product = self * y_axis_vector

        self_length = self.get_length()
        if self_length == 0:
            return 0

        cos_a = dot_product / (self_length * y_axis_vector.get_length())
        cos_a = max(-1.0, min(1.0, cos_a))

        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)

        if self.x < 0:
            return int(360 - angle_deg)
        else:
            return int(angle_deg)

    def rotate(self, degrees: int) -> 'Vector':
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        rotated_x = self.x * cos_a - self.y * sin_a
        rotated_y = self.x * sin_a + self.y * cos_a

        return Vector(rotated_x, rotated_y)
