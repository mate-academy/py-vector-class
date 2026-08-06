import math


class Vector:
    def __init__(self, x_coo: float, y_coo: float) -> None:
        self.x = round(x_coo, 2)
        self.y = round(y_coo, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: "Vector") -> "Vector" or float:
        if isinstance(other, (int, float)):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> "Vector":
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitudes_product = self.get_length() * other.get_length()

        if magnitudes_product != 0:
            cosine_angle = dot_product / magnitudes_product
            if cosine_angle > 1:
                cosine_angle = 1
            elif cosine_angle < -1:
                cosine_angle = -1

            angle_radians = math.acos(cosine_angle)
            angle_degrees = math.degrees(angle_radians)

            return round(angle_degrees)

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = int(math.degrees(angle_radians))
        return abs(angle_degrees)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
