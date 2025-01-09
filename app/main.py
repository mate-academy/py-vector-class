import math


class Vector:
    def __init__(self, x_mean: float, y_mean: float) -> None:
        self.x = round(x_mean, 2)
        self.y = round(y_mean, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: ("Vector", float)) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        x_value = self.x / Vector.get_length(self)
        y_value = self.y / Vector.get_length(self)
        return Vector(x_value, y_value)

    def angle_between(self, other: "Vector") -> int:
        angle = (self * other) / (Vector.get_length(self)
                                  * Vector.get_length(other))
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> int:
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, degree: int) -> "Vector":
        degree_to_radians = math.radians(degree)
        x_value = (math.cos(degree_to_radians)) * self.x - \
                  (math.sin(degree_to_radians)) * self.y
        y_value = (math.sin(degree_to_radians)) * self.x + \
                  (math.cos(degree_to_radians)) * self.y
        return Vector(x_value, y_value)
