import math


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> int | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: set,
            end_point: set) -> "Vector":

        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: int) -> int | float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        cos_angle = dot_product / lengths_product
        angle_radians = math.acos(cos_angle)
        return round(math.degrees(angle_radians))

    def get_angle(self) -> int | float:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)

        if angle_degrees <= 0:
            return round(abs(angle_degrees))

    def rotate(self, degrees: int | float) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
