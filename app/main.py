import math


class Vector:
    def __init__(self,
                 x_coordinate: float,
                 y_coordinate: float
                 ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]
                                    ) -> "Vector":
        x_difference = end_point[0] - start_point[0]
        y_difference = end_point[1] - start_point[1]
        return cls(x_difference, y_difference)


    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        vector = Vector(0, abs(self.y))
        angle = self * vector / (self.get_length() * vector.get_length())
        angle_in_degree = math.degrees(math.acos(angle))
        return round(angle_in_degree)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)


    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" or float) -> "Vector" or float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)
