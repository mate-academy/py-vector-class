import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def create_vector_by_two_points(
        self, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_diff = end_point[0] - start_point[0]
        y_diff = end_point[1] - start_point[1]
        return self.__class__(x_diff, y_diff)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_angle = dot_product / length_product
        angle_rad = math.acos(cos_angle)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        self.x = round(new_x, 2)
        self.y = round(new_y, 2)
        return self
