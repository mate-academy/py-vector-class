import math


class Vector:
    def __init__(self, x: float , y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> "Vector":
        if (isinstance(start_point[0], (int, float))
                and isinstance(start_point[1], (int, float))
                and isinstance(end_point[0], (int, float))
                and isinstance(end_point[1], (int, float))):
            x1, y1 = start_point
            x2, y2 = end_point
            return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(round(normalized_x, 2), round(normalized_y, 2))

    def angle_between(self, other: "Vector") -> int:

        if self.get_length() != 0 and other.get_length() != 0:
            cos_a = (self * other) / (self.get_length() * other.get_length())
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:

        if self.get_length() != 0:
            angle_cos = self.y / self.get_length()
            return round(math.degrees(math.acos(angle_cos)))

    def rotate(self, degrees: int) -> "Vector":

        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(round(new_x, 2), round(new_y, 2))
