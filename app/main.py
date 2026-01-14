import math


class Vector:
    def __init__(self, x1: float, y2: float) -> None:
        self.x: float = round(x1, 2)
        self.y: float = round(y2, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type."
                            " Vector can only be added to another Vector.")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            raise TypeError("Unsupported operand type."
                            "Vector can only be subtracted by another Vector.")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x1 = round(end_point[0] - start_point[0], 2)
        y2 = round(end_point[1] - start_point[1], 2)
        return cls(x1, y2)

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 16)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, vector: "Vector") -> int:
        dot_product = self * vector
        self_length = self.get_length()
        vector_length = vector.get_length()
        cos_a = dot_product / (self_length * vector_length)
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)  # Positive Y axis
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = round(self.x * math.cos(radians)
                      - self.y * math.sin(radians), 2)
        new_y = round(self.x * math.sin(radians)
                      + self.y * math.cos(radians), 2)
        return Vector(new_x, new_y)
