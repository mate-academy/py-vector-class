import math


class Vector:
    def __init__(self, vector_x: int, vector_y: int) -> None:
        self.vector_x = round(vector_x, 2)
        self.vector_y = round(vector_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            vector_x=self.vector_x + other.vector_x,
            vector_y=self.vector_y + other.vector_y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            vector_x=self.vector_x - other.vector_x,
            vector_y=self.vector_y - other.vector_y
        )

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.vector_x * other, self.vector_y * other)
        elif isinstance(other, Vector):
            return self.vector_x * other.vector_x + self.vector_y * other.vector_y

    @classmethod
    def create_vector_bvector_y_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(pow(self.vector_x, 2) + pow(self.vector_y, 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.vector_x / length, self.vector_y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_a = ((self.vector_x * other.vector_x + self.vector_y * other.vector_y)
                 / (self.get_length() * other.get_length()))
        radians = math.acos(cos_a)
        return round(math.degrees(radians), 0)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_vector_x = (self.vector_x * math.cos(radians)
                 - self.vector_y * math.sin(radians))
        new_vector_y = (self.vector_x * math.sin(radians)
                 + self.vector_y * math.cos(radians))
        return Vector(new_vector_x, new_vector_y)
