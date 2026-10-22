import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + other.x,
            y_coordinate=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - other.x,
            y_coordinate=self.y - other.y
        )

    def __mul__(self, other: Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmul__(self, other: Vector) -> Vector | int | float:
        return self.__mul__(other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float],
                                    end_point: tuple[float]) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot = self * other
        length_product = self.get_length() * other.get_length()
        cos_angle = dot / length_product
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float:
        angle = abs(math.degrees(math.atan2(self.x, self.y)))
        return round(angle)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)
