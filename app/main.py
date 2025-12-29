import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, vector: "Vector") -> "Vector":
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: "Vector") -> "Vector":
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(
        self, vector: int | float | "Vector"
    ) -> int | float | "Vector":
        if isinstance(vector, Vector):
            return self.x * vector.x + self.y * vector.y
        return Vector(round(self.x * vector, 2), round(self.y * vector, 2))

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, vector: "Vector") -> int:
        agle = math.degrees(
            math.acos(self.__mul__(vector)
                      / (self.get_length() * vector.get_length()))
        )
        return round(agle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)
