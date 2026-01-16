import math


class Vector:
    def __init__(self, x_val: float, y_val: float) -> None:
        self.x = round(x_val, 2)
        self.y = round(y_val, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: ["Vector", float, int]) -> ["Vector", float, int]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int | float):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return Vector(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        normalized_x = round(self.x / self.get_length(), 2)
        normalized_y = round(self.y / self.get_length(), 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.__mul__(other)
        cosine_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cosine_angle)
        return round(math.degrees(angle_in_radians))

    def get_angle(self) -> int:
        angle_in_radians = math.atan2(self.x, self.y)
        return abs(round(math.degrees(angle_in_radians)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(rotated_x, rotated_y)
