import math


class Vector:
    def __init__(self, coordinates_x: float, coordinates_y: float) -> None:
        self.x = round(coordinates_x, 2)
        self.y = round(coordinates_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: "Vector" or int or float
    ) -> "Vector" or int or float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        start = start_point
        end = end_point
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> int or float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()

        if magnitude_product != 0:
            cosine_angle = dot_product / magnitude_product
            angle_in_radians = math.acos(cosine_angle)
            angle_in_degrees = math.degrees(angle_in_radians)
            return round(angle_in_degrees)

        return 0

    def get_angle(self) -> float or int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int or float) -> "Vector":
        angle_in_radians = math.radians(degrees)
        rotated_x = self.x * math.cos(angle_in_radians) - \
            self.y * math.sin(angle_in_radians)
        rotated_y = self.x * math.sin(angle_in_radians) + \
            self.y * math.cos(angle_in_radians)
        return Vector(rotated_x, rotated_y)
