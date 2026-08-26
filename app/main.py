import math


class Vector:
    def __init__(self, x_vector: (int, float), y_vector: (int, float)) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        if isinstance(start_point, tuple) and isinstance(end_point, tuple):
            return cls(end_point[0] - start_point[0],
                       end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length != 0:
            normalized_x = self.x / length
            normalized_y = self.y / length
        else:
            normalized_x = 0
            normalized_y = 0
        return Vector(round(normalized_x, 2), round(normalized_y, 2))

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        vector_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        vector_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(vector_x, vector_y)
