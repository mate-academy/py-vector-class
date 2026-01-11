class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float | int:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        import math

        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        y_asix = Vector(0, 1000)
        return self.angle_between(y_asix)

    def rotate(self, alpha: int) -> Vector:
        import math

        x_coord = self.x
        y_coord = self.y
        alpha = math.radians(alpha)
        cos_a = math.cos(alpha)
        sin_a = math.sin(alpha)
        return Vector(
            x_coord * cos_a - y_coord * sin_a,
            x_coord * sin_a + y_coord * cos_a
        )
