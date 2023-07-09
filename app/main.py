class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector((self.x + other.x)(self.y + other.y))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector((self.x - other.x)(self.y - other.y))

    def __mul__(self, other: "Vector") -> "Vector":
        return Vector(
            (self.x * other.x) + (self.y * other.y))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float], end_point: tuple[float]) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(round(x, 2), round(y, 2))

    def get_length(self) -> "Vector":
        pass

    def get_normalized(self) -> "Vector":
        pass

    def angle_between(self) -> int | float:

        return degrees
        pass

    def rotate(degrees: int | float) -> "Vector":
        pass
