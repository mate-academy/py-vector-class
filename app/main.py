import math


class Vector:
    def __init__(self, xw: float, yw: float) -> None:
        self.x = round(xw, 2)
        self.y = round(yw, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number: int) -> float:
        if type(number) == int or type(number) == float:
            return Vector(self.x * number, self.y * number)
        if isinstance(number, Vector):
            return self.x * number.x + self.y * number.y

    def __str__(self: int) -> str:
        return f"({self.x}, {self.y})"

    @classmethod
    def create_vector_by_two_points(cls, p1: int,
                                    p2: int) -> float:
        return cls((p2[0] - p1[0]), (p2[1] - p1[1]))

    def get_length(self: int) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self: int) -> float:
        return Vector(self.x / (math.sqrt
                      (self.x ** 2 + self.y**2)), self.y
                      / (math.sqrt(self.x ** 2 + self.y**2)))

    def angle_between(self, number: int) -> float:
        return round(math.degrees(math.acos((self.x * number.x + self.y
                     * number.y) / (math.sqrt(self.x ** 2 + self.y ** 2)
                     * math.sqrt(number.x ** 2 + number.y ** 2)))), 0)

    def dot(self, other: int) -> float:
        return self.x * other.x + self.y * other.y

    def get_angle(self: int) -> float:
        y_axis_vector = Vector(0, 1)
        dot_product = self.dot(y_axis_vector)
        lengths_product = self.get_length() * y_axis_vector.get_length()
        cos_angle = dot_product / lengths_product
        angle_radians = math.acos(cos_angle)
        angle_degrees = round(math.degrees(angle_radians), 0)
        return angle_degrees

    def rotate(self, angle_degrees: int) -> float:
        angle_radians = math.radians(angle_degrees)
        cos_theta = math.cos(angle_radians)
        sin_theta = math.sin(angle_radians)
        x_rotated = self.x * cos_theta - self.y * sin_theta
        y_rotated = self.x * sin_theta + self.y * cos_theta
        return Vector(x_rotated, y_rotated)
