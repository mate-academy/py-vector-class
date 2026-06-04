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
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        return round(
            math.ceil(math.degrees(math.acos(
                (self.x * other.x + self.y * other.y)
                / (
                    math.sqrt(self.x ** 2 + self.y ** 2)
                    * math.sqrt(other.x ** 2 + other.y ** 2)
                )
            ))), 2
        )

    def get_angle(self) -> int:
        return int(
            math.degrees(
                math.acos(self.y / math.sqrt(self.x ** 2 + self. y ** 2))
            )
        )

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            (self.x * math.cos(math.radians(degrees)))
            - (self.y * math.sin(math.radians(degrees))),
            (self.x * math.sin(math.radians(degrees)))
            + (self.y * math.cos(math.radians(degrees)))
        )
