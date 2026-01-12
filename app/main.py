import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

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

    def __mul__(self, other: "Vector | float") -> "Vector | float":
        if isinstance(other, Vector):
            # dot product
            return self.x * other.x + self.y * other.y
        else:
            # scalar multiplication
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_delta = end_point[0] - start_point[0]
        y_delta = end_point[1] - start_point[1]
        return cls(x_delta, y_delta)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_angle = max(min(dot_product / length_product, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(-self.x, self.y))
        if angle < 0:
            angle += 360
        return round(angle)

    def rotate(self, degrees_value: int) -> "Vector":
        radians_value = math.radians(degrees_value)
        cos_r = math.cos(radians_value)
        sin_r = math.sin(radians_value)
        x_new = self.x * cos_r - self.y * sin_r
        y_new = self.x * sin_r + self.y * cos_r
        return Vector(
            round(x_new, 2),
            round(y_new, 2)
        )

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
