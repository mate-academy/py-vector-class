from math import sqrt, hypot, degrees, acos, sin, cos


class Vector:

    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]
                                    ) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        if self.get_length() == 0:
            return None
        length = hypot(self.x, self.y)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_p = self.x * other.x + self.y * other.y
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            return None
        cos_a = max(-1, min(1, dot_p / (len_other * len_self)))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> "Vector":
        dot_p = self.x * 0 + self.y * 1
        len_self = self.get_length()
        len_other = 1
        if len_self == 0 :
            return None
        cos_a = max(-1, min(1, dot_p / (len_other * len_self)))
        return round(degrees(acos(cos_a)))

    def rotate(self, b_value: float) -> "Vector":
        rad = b_value * (3.141592653589793 / 180)
        cos_b = cos(rad)
        sin_b = sin(rad)
        return Vector(
            self.x * cos_b - self.y * sin_b,
            self.x * sin_b + self.y * cos_b
        )
