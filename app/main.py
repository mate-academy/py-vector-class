import math


class Vector:
    # write your code here
    def __init__(self, xx: int, yy: int) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: None) -> None:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: None) -> None:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: None) -> None:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: float, end_point: float) -> None:
        xx = end_point[0] - start_point[0]
        yy = end_point[1] - start_point[1]
        return cls(xx, yy)

    def get_length(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> None:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int) -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> None:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
