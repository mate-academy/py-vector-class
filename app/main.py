import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

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
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        lengths_product = self.get_length() * vector.get_length()
        cosine_angle = dot_product / lengths_product

        return round(math.degrees(math.acos(cosine_angle)))

    def get_angle(self) -> int:
        positive_y_axis_vector = Vector(0, 1)
        return self.angle_between(positive_y_axis_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        rotated_x = (
            self.x * math.cos(radians)
            - self.y * math.sin(radians)
        )
        rotated_y = (
            self.x * math.sin(radians)
            + self.y * math.cos(radians)
        )

        return Vector(rotated_x, rotated_y)
