import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]

        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()

        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector

        cos_a = dot_product / (
            self.get_length() * vector.get_length()
        )

        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)

        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )

        y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(x, y)
