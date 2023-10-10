import math

class Vector:
    def __init__(self, vector_x: int, vector_y: int) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            vector_x=self.x + other.x,
            vector_y=self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            vector_x=self.x - other.x,
            vector_y=self.y - other.y
        )

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_a = ((self.x * other.x + self.y * other.y)
                 / (self.get_length() * other.get_length()))
        radians = math.acos(cos_a)
        return round(math.degrees(radians), 0)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_vector_x = (self.x * math.cos(radians)
                 - self.y * math.sin(radians))
        new_vector_y = (self.x * math.sin(radians)
                 + self.y * math.cos(radians))
        return Vector(new_vector_x, new_vector_y)
