import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, another: "Vector") -> "Vector":
        x_sum = self.x + another.x
        y_sum = self.y + another.y
        return Vector(x_sum, y_sum)

    def __sub__(self, another: "Vector") -> "Vector":
        x_diff = self.x - another.x
        y_diff = self.y - another.y
        return Vector(x_diff, y_diff)

    def __mul__(self, another: float) -> float:
        if isinstance(another, Vector):
            return self.x * another.x + self.y * another.y
        elif isinstance(another, (float, int)):
            return Vector(self.x * another, self.y * another)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_start, y_start = start_point
        x_end, y_end = end_point
        x_diff = x_end - x_start
        y_diff = y_end - y_start
        return cls(x_diff, y_diff)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, another: "Vector") -> float:
        dot_product = self * another
        length_self = self.get_length()
        length_other = another.get_length()

        if length_self == 0 or length_other == 0:
            return 0

        cos_angle = dot_product / (length_self * length_other)
        cos_angle = max(-1, min(1, cos_angle))
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> float:
        length_self = self.get_length()
        if length_self == 0:
            return 0
        cos_angle = self.y / length_self
        cos_angle = max(-1, min(1, cos_angle))
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_rotated = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_rotated = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_rotated, y_rotated)
