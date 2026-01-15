import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: object) -> object:
        vector = Vector((self.x + other.x), (self.y + other.y))
        return vector

    def __sub__(self, other: object) -> object:
        vector = Vector((self.x - other.x), (self.y - other.y))
        return vector

    def __mul__(self, other: object) -> object:
        if isinstance(other, (int, float)):
            return Vector((self.x * other), (self.y * other))
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: list,
                                    end_point: list) -> object:
        return cls(
            (end_point[0] - start_point[0]),
            (end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        return length

    def get_normalized(self) -> object:
        normalized = Vector((self.x / (self.x ** 2 + self.y ** 2) ** 0.5),
                            (self.y / (self.x ** 2 + self.y ** 2) ** 0.5)
                            )
        return normalized

    def angle_between(self, vector: object) -> object:
        normalized1 = Vector(
            (self.x / (self.x ** 2 + self.y ** 2) ** 0.5),
            (self.y / (self.x ** 2 + self.y ** 2) ** 0.5)
        )
        normalized2 = Vector(
            (vector.x / (vector.x ** 2 + vector.y ** 2) ** 0.5),
            (vector.y / (vector.x ** 2 + vector.y ** 2) ** 0.5)
        )
        angle = math.ceil(math.degrees(math.acos(normalized1 * normalized2)))
        return angle

    def get_angle(self) -> object:
        normalized_vector = Vector(
            (self.x / (self.x ** 2 + self.y ** 2) ** 0.5),
            (self.y / (self.x ** 2 + self.y ** 2) ** 0.5)
        )
        y_axis = Vector(0, 1)
        angle = math.floor(math.degrees(math.acos(normalized_vector * y_axis)))
        return angle

    def rotate(self, degrees: int) -> object:
        q_point = self.x * math.cos(math.radians(degrees))
        w_point = self.y * math.sin(math.radians(degrees))
        e_point = self.x * math.sin(math.radians(degrees))
        r_point = self.y * math.cos(math.radians(degrees))
        result = Vector((q_point - w_point), (e_point + r_point))

        return result
