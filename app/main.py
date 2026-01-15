import math


class Vector:
    def __init__(self, x_point: float, y_poin: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_poin, 2)

    def __add__(self, other: object) -> object:
        return Vector(
            x_point=self.x + other.x,
            y_poin=self.y + other.y
        )

    def __sub__(self, other: object) -> object:
        return Vector(
            x_point=self.x - other.x,
            y_poin=self.y - other.y
        )

    def __mul__(self, other: object) -> object | float:
        if isinstance(other, float | int):
            return Vector(
                x_point=self.x * other,
                y_poin=self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        return cls(
            x_point=end_point[0] - start_point[0],
            y_poin=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        normalized_x = self.x / length
        normalized_y = self.y / length
        return Vector(normalized_x, normalized_y)

    def dot_product(self, other : object) -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: object) -> int:
        dot_prod = self.dot_product(other)
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_theta = dot_prod / (length_self * length_other)
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
