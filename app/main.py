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
            # Scalar multiplication
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            # Dot product
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> "Vector":
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        cos_a = min(1, max(-1, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        # Angle with positive Y axis
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(new_x, new_y)
