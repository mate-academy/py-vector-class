import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        x_coord = self.x / self.get_length()
        y_coord = self.y / self.get_length()

        return Vector(x_coord, y_coord)

    def angle_between(self, other: Vector) -> float:
        cos_theta = (self * other) / (self.get_length() * other.get_length())

        return math.ceil(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        return math.floor(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: float) -> Vector:
        x_coord = ((math.cos(math.radians(degrees)) * self.x)
                   - (math.sin(math.radians(degrees)) * self.y))
        y_coord = ((math.sin(math.radians(degrees)) * self.x)
                   + (math.cos(math.radians(degrees)) * self.y))

        return Vector(x_coord, y_coord)
