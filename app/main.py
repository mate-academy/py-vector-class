import math


class Vector:
    def __init__(self, x_cordinate: float, y_cordinate: float) -> None:
        self.x = round(float(x_cordinate), 2)
        self.y = round(float(y_cordinate), 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x
                           + self.y * other.y)
            return dot_product
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(), self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        dot = self * other
        length = self.get_length() * other.get_length()
        cos_a = dot / length
        angle = math.degrees(math.acos(cos_a))
        return round(angle, 0)

    def get_angle(self) -> float:
        y_cordinate = Vector(0, 1)
        our_angle = self.angle_between(y_cordinate)
        return our_angle

    def rotate(self, angle: int) -> Vector:
        rotation_in_radians = math.radians(angle)
        return Vector(
            self.x * math.cos(rotation_in_radians)
            - self.y * math.sin(rotation_in_radians),
            self.x * math.sin(rotation_in_radians)
            + self.y * math.cos(rotation_in_radians)
        )
