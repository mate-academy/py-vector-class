from math import degrees, acos, cos, sin, radians, sqrt


class Vector:
    def __init__(self, x_cord: (int, float), y_cord: (int, float)) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: (int, float)) -> object:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2))

    def __sub__(self, other: object) -> object:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2))

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_cord: tuple,
            end_cord: tuple) -> "Vector":
        return cls(
            round(end_cord[0] - start_cord[0], 2),
            round(end_cord[1] - start_cord[1], 2)
        )

    def get_length(self) -> object:
        return sqrt((self.x - 0) ** 2 + (self.y - 0) ** 2)

    def get_normalized(self) -> "Vector":
        x_c = self.x / Vector.get_length(self)
        y_c = self.y / Vector.get_length(self)
        return Vector(round(x_c, 2), round(y_c, 2))

    def angle_between(self, other: "Vector") -> int:
        cos_temp = (Vector.__mul__(self, other)) / \
            (Vector.get_length(self) * abs(Vector.get_length(other)))
        return round(degrees(acos(cos_temp)))

    def get_angle(self) -> float:
        return round(degrees(acos((self.y * 1) / (Vector.get_length(self)))))

    def rotate(self, angle: int) -> "Vector":
        x_c = round(self.x * cos(radians(angle))
                    - self.y * sin(radians(angle)), 2)
        y_c = round(self.x * sin(radians(angle))
                    + self.y * cos(radians(angle)), 2)
        return Vector(x_c, y_c)
