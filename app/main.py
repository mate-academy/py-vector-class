import math


class Vector:
    def __init__(self, x: int, y: int) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int | float) -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: int | float) -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: int | float) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        x = end_point[0] - start_point[0]  # noqa: VNE001
        y = end_point[1] - start_point[1]  # noqa: VNE001
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        normalized_x = self.x / self.get_length()
        normalized_y = self.y / self.get_length()
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self.x * other.x + self.y * other.y
        length_product = self.get_length() * other.get_length()

        cos_theta = dot_product / length_product
        angle_radians = math.acos(max(-1, min(1, cos_theta)))

        return round(math.degrees(angle_radians))

    def get_angle(self) -> float:
        length = self.get_length()

        cos_theta = self.y / length
        angle_radians = math.acos(cos_theta)
        return round(math.degrees(angle_radians))

    def rotate(self, degrees: int) -> "Vector":
        theta = math.radians(degrees)

        new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        new_y = self.x * math.sin(theta) + self.y * math.cos(theta)

        return Vector(round(new_x, 2), round(new_y, 2))
