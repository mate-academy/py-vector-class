import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

        self.vector_x = self.x
        self.vector_y = self.y

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: "Vector | int | float") -> "Vector | float":
        if isinstance(other, Vector):
            return (
                (self.x * other.x)
                + (self.y * other.y)
            )
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError(
            "A multiplicação só é suportada entre"
            "dois Vetores ou um Vetor e um número."
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":

        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return math.sqrt(self.vector_x**2 + self.vector_y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.vector_x / length, self.vector_y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()

        if lengths_product == 0:
            return 0

        cos_a = dot_product / lengths_product
        cos_a = max(-1.0, min(1.0, cos_a))

        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)

        new_x = (
            (self.vector_x * math.cos(rad)) - (self.vector_y * math.sin(rad))
        )

        new_y = (
            (self.vector_x * math.sin(rad)) + (self.vector_y * math.cos(rad))
        )
        return Vector(new_x, new_y)
