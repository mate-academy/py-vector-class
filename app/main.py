from math import sqrt, acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: int | float) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return NotImplemented

    def __sub__(self, other: int | float) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            NotImplemented

    def __mul__(self, other: int | float) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> float:
        return Vector(
            self.x / sqrt(self.x ** 2 + self.y ** 2),
            self.y / sqrt(self.x ** 2 + self.y ** 2)
        )

    def angle_between(self, vector: "Vector") -> int:
        dot_prod = self.x * vector.x + self.y * vector.y
        length_self = self.get_length()
        length_vector = vector.get_length()
        cos_theta = dot_prod / (length_self * length_vector)
        theta = acos(cos_theta)
        return round(degrees(theta))

    def get_angle(self) -> int:
        return round(degrees(acos(self.y / self.get_length())))

    def rotate(self, degrees: float | int) -> "Vector":
        radians_angle = radians(degrees)
        return Vector(
            (cos(radians_angle) * self.x) - (sin(radians_angle) * self.y),
            (sin(radians_angle) * self.x) + (cos(radians_angle) * self.y)
        )
