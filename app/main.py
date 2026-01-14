import math


class Vector :
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other_vector: "Vector") -> "Vector":
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def __sub__(self, other_vector: "Vector") -> "Vector":
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":  # noqa: E501
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])  # noqa: E501

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector: "Vector") -> int:
        dot_product = self * other_vector
        cos_angle = dot_product / (self.get_length() * other_vector.get_length())  # noqa: E501
        angle_radians = math.acos(cos_angle)
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees

    def get_angle(self) -> int:
        return abs(int(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
