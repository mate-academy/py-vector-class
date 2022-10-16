import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: (int, float)) -> "Vector":
        if isinstance(other, (float, int)):
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)
        else:
            result = self.x * other.x + self.y * other.y
            return result

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        inversion_length = 1 / self.get_length()
        new_x = self.x * inversion_length
        new_y = self.y * inversion_length
        return Vector(new_x, new_y)

    def angle_between(self, other_vector: "Vector") -> int:
        scalar_prod = self.x * other_vector.x + self.y * other_vector.y
        cos_a = scalar_prod / (self.get_length() * other_vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(
            math.degrees(math.acos((self.y * 1) / (Vector.get_length(self))))
        )

    def rotate(self, angle: int) -> "Vector":
        x_c = round(self.x * math.cos(math.radians(angle))
                    - self.y * math.sin(math.radians(angle)), 2)
        y_c = round(self.x * math.sin(math.radians(angle))
                    + self.y * math.cos(math.radians(angle)), 2)
        return Vector(x_c, y_c)
