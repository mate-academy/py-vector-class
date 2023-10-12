import math


class Vector:
    def __init__(self, x_vector: int, y_vector: int) -> None:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> "Vector":
        vector_len = self.get_length()
        return Vector(self.x / vector_len, self.y / vector_len)

    def angle_between(self, other: "Vector") -> int:
        mul_vectors = self * other
        len_vectors = self.get_length() * other.get_length()
        return round((math.degrees(math.acos(mul_vectors / len_vectors))))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        rounded_angle_deg = round(angle_deg)
        return abs(rounded_angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        radian = math.radians(degrees)
        new_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(new_x, new_y)
