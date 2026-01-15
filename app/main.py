import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # No rounding here
        else:
            raise TypeError(
                "Unsupported operand type(s) for *: 'Vector' and '{}'"
                .format(type(other).__name__)
            )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> "Vector":
        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        dot = self * vector
        len_self = self.get_length()
        len_other = vector.get_length()
        if len_self == 0 or len_other == 0:
            return 0
        cos_a = max(-1, min(1, dot / (len_self * len_other)))
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0
        nx = self.x / length
        ny = self.y / length

        dot = ny
        det = -nx

        angle = math.degrees(math.acos(dot))
        if det < 0:
            angle = 360 - angle

        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
