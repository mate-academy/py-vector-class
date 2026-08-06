import math


class Vector:
    def __init__(self, line_one: float, line_two: float) -> None:
        self.x = round(line_one, 2)
        self.y = round(line_two, 2)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        normalized_x = round(self.x / length, 2)
        normalized_y = round(self.y / length, 2)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self.x * other.x + self.y * other.y
        self_length = self.get_length()
        other_length = other.get_length()
        cosine = dot_product / (self_length * other_length)
        angle_radians = math.acos(cosine)
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees

    def get_angle(self) -> float:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = round(
            self.x * math.cos(radians) - self.y * math.sin(radians), 2
        )
        rotated_y = round(
            self.x * math.sin(radians) + self.y * math.cos(radians), 2
        )
        return Vector(rotated_x, rotated_y)

    def dot_product(self, other: "Vector") -> float:
        return round(self.x * other.x + self.y * other.y, 4)

    def __add__(self, other: "Vector") -> "Vector":
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: "Vector") -> "Vector":
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: ["Vector", int, float]) -> ["Vector", int, float]:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        elif isinstance(other, (int, float)):
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type "
                            "for multiplication.")

    @staticmethod
    def create_vector_by_two_points(
            start_point: float,
            end_point: float
    ) -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        vector_x = round(end_x - start_x, 2)
        vector_y = round(end_y - start_y, 2)
        return Vector(vector_x, vector_y)
