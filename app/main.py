import math


class Vector:

    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_1 = self.get_length()
        length_2 = other.get_length()
        cos_a = dot_product / (length_1 * length_2)
        cos_a = max(-1, min(cos_a, 1))
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(-self.x, self.y))
        if angle < 0:
            angle += 360

        return round(angle)

    def rotate(self, degrees: float | int) -> "Vector":
        radians = math.radians(degrees)

        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(x_new, y_new)
