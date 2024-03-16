import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" or float) -> float or "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cosine_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cosine_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)  # Positive Y axis
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        angle_in_radians = math.radians(degrees)
        rotated_x = (self.x * math.cos(angle_in_radians)
                     - self.y * math.sin(angle_in_radians))
        rotated_y = (self.x * math.sin(angle_in_radians)
                     + self.y * math.cos(angle_in_radians))
        return Vector(rotated_x, rotated_y)
