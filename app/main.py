from math import degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ):
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        length = self.get_length()
        return Vector(
            x=self.x / length,
            y=self.y / length
        )

    def angle_between(self, other) -> int:
        return round(degrees(acos(
            (self.__mul__(other)) / (self.get_length() * other.get_length())
        )))

    def get_angle(self):
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int):
        radian = radians(degree)
        return Vector(
            x=self.x * cos(radian) - self.y * sin(radian),
            y=self.y * cos(radian) + self.x * sin(radian)
        )
