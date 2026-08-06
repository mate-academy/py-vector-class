import math


class Vector:
    def __init__(self, x1: float, y1: float) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise ValueError("Cannot add Vector with a non-Vector object.")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise ValueError(
                "Cannot subtract Vector with a non-Vector object.")

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise ValueError(
                "Cannot multiply Vector with a non-Vector object.")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point:
            tuple[float, float], end_point: tuple[float, float]) -> "Vector":
        return Vector(end_point[0]
                      - start_point[0], end_point[1] - start_point[1])

    create_vector_by_two_points = classmethod(create_vector_by_two_points)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        degrees = round(math.degrees(math.acos(cos_a)))
        return degrees

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.y * cos_a + self.x * sin_a
        return Vector(new_x, new_y)
