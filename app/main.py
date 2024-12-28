import math


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.vector_x = round(vector_x, 2)
        self.vector_y = round(vector_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.vector_x + other.vector_x, self.vector_y
                      + other.vector_y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.vector_x - other.vector_x, self.vector_y
                      - other.vector_y)

    def __mul__(self, other: "Vector") -> "Vector" | float:
        if isinstance(other, (int, float)):
            return Vector(self.vector_x * other, self.vector_y * other)
        elif isinstance(other, Vector):
            dot_product = (self.vector_x * other.vector_x + self.vector_y
                           * other.vector_y)
            return round(dot_product, 4)
        else:
            raise TypeError("Unsupported operation for * with type {}".
                            format(type(other)))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return cls(vector_x, vector_y)

    def get_length(self) -> float:
        return math.sqrt(self.vector_x ** 2 + self.vector_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        else:
            return Vector(self.vector_x / length, self.vector_y / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            raise ValueError("Cannot calculate angle with a "
                             "zero-length vector.")
        cos_angle = max(min(dot_product / lengths_product, 1), -1)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float:
        reference = Vector(0, 1)
        return self.angle_between(reference)

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        new_x = (self.vector_x * math.cos(radians) - self.vector_y
                 * math.sin(radians))
        new_y = (self.vector_x * math.sin(radians) + self.vector_y
                 * math.cos(radians))
        return Vector(new_x, new_y)
