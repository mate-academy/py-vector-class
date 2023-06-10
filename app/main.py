import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]
                                    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        x_coord: float = round(end_x - start_x, 2)
        y_coord: float = round(end_y - start_y, 2)
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos_a: float = \
            (self * other) / (self.get_length() * other.get_length())
        degrees: int = round(math.degrees(math.acos(cos_a)))
        return degrees

    def get_angle(self) -> int:
        reference_vector: Vector = Vector(0, 1)  # Positive Y-axis
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians: float = math.radians(degrees)
        cos_theta: float = math.cos(radians)
        sin_theta: float = math.sin(radians)

        new_x: float = self.x * cos_theta - self.y * sin_theta
        new_y: float = self.x * sin_theta + self.y * cos_theta

        return Vector(new_x, new_y)
